# Importing necessary libraries and packages
from enum import Enum
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoFeatureExtractor, DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch
import sqlite3

# Enumerated types for CRUD operations
class CRUD(Enum):
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    DELETE = 'delete'

# Constants for table names and columns
CONVERSATION_HISTORY_TABLE = 'conversation_history'
OBJECT_COUNTS_TABLE = 'object_counts'
CONVERSATION_COLUMNS = 'id INTEGER PRIMARY KEY AUTOINCREMENT, user_input TEXT, llama_response TEXT'
OBJECT_COUNT_COLUMNS = 'id INTEGER PRIMARY KEY AUTOINCREMENT, query TEXT, count INTEGER'

# DatabaseAgent class for handling CRUD operations
class DatabaseAgent:
    """
    DatabaseAgent class for handling CRUD operations with a SQLite database.
    
    Attributes:
    - conn (sqlite3.Connection): The SQLite database connection.
    
    Methods:
    - close_connection: Close the SQLite database connection.
    """
    def __init__(self, db_name):
        """
        Initialize DatabaseAgent and establish a database connection.
        
        Parameters:
        - db_name (str): The name of the SQLite database.
        """
        self.conn = sqlite3.connect(db_name)
        
    def close_connection(self):
        """
        Close the SQLite database connection.
        """
        if self.conn:
            self.conn.close()

# MultimodalAssistant class for handling text-based and image-based user queries
class MultimodalAssistant:
    """
    MultimodalAssistant class for handling text-based and image-based user queries.
    
    Attributes:
    - llama_tokenizer (AutoTokenizer): Tokenizer for the LLAMA language model.
    - llama_model (AutoModelForCausalLM): Pre-trained LLAMA language model for text-based queries.
    - extractor (DetrImageProcessor): Image processor for the DETR model.
    - detr_model (DetrForObjectDetection): Pre-trained DETR model for image-based queries.
    - session_memory (dict): Dictionary to store the conversation history and object count results.
    - db_agent (DatabaseAgent): Database agent for handling CRUD operations.
    
    Methods:
    - initialize_database: Initialize the SQLite database tables if they do not exist.
    - db_handler: Handles all database interactions for CRUD operations.
    """
    
    def __init__(self, db_name="assistant.db"):
        """
        Initialize MultimodalAssistant and establish a database connection.
        
        Parameters:
        - db_name (str): The name of the SQLite database. Default is "assistant.db".
        """
        self.llama_tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
        self.llama_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
        self.extractor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
        self.detr_model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")
        self.session_memory = {"conversation": [], "object_counts": {}}
        self.db_agent = DatabaseAgent(db_name)
        self.initialize_database()
        
    def initialize_database(self):
        """
        Initialize the SQLite database tables if they do not already exist.
        """
        with self.db_agent.conn:
            self.db_agent.conn.execute(f"CREATE TABLE IF NOT EXISTS {CONVERSATION_HISTORY_TABLE} ({CONVERSATION_COLUMNS});")
            self.db_agent.conn.execute(f"CREATE TABLE IF NOT EXISTS {OBJECT_COUNTS_TABLE} ({OBJECT_COUNT_COLUMNS});")
            
    def db_handler(self, operation, table_name, **kwargs):
        """
        Handles all database interactions for CRUD operations.
        
        Parameters:
        - operation (str): CRUD operation to be performed ('create', 'insert', 'update', 'delete').
        - table_name (str): The name of the table to operate on.
        - kwargs (dict): Additional keyword arguments for CRUD operations.
        """
        operation_type = CRUD(operation).value
        with self.db_agent.conn:
            if operation_type == CRUD.CREATE.value:
                self.db_agent.conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({kwargs.get('columns', '')});")
            elif operation_type == CRUD.INSERT.value:
                self.db_agent.conn.execute(f"INSERT INTO {table_name} ({kwargs.get('columns', '')}) VALUES ({kwargs.get('values', '')});")
            elif operation_type == CRUD.UPDATE.value:
                self.db_agent.conn.execute(f"UPDATE {table_name} SET {kwargs.get('updates', '')} WHERE {kwargs.get('condition', '')};")
            elif operation_type == CRUD.DELETE.value:
                self.db_agent.conn.execute(f"DELETE FROM {table_name} WHERE {kwargs.get('condition', '')};")
                
    def handle_text_query(self, user_input):
        """
        Handles a text-based query and updates the session memory and database.

        Parameters:
        - user_input (str): The text-based query from the user.
        """
        output_text = self.process_text(user_input)
        self.session_memory['conversation'].append({"llama": output_text})
        self.db_handler(CRUD.UPDATE.value, CONVERSATION_HISTORY_TABLE, updates=f'llama_response="{output_text}"', condition=f'user_input="{user_input}"')
        print(f"LLAMA Response: {output_text}")
        
    def handle_image_query(self, user_input):
        """
        Handles an image-based query and updates the session memory and database.

        Parameters:
        - user_input (str): The image-based query from the user, which includes the image path.
        """
        image_path = user_input.split(" ")[-1]
        detected_objects = self.count_objects(image_path)
        self.session_memory['object_counts'][user_input] = detected_objects
        self.db_handler(CRUD.INSERT.value, OBJECT_COUNTS_TABLE, columns='query, count', values=f'"{user_input}", {detected_objects}')
        print(f"DETR Detected Objects: {detected_objects}")
    
    def session_handler(self):
        """
        Manages the interactive session, handling both text and image queries.
        
        The method runs an infinite loop, waiting for user input. Depending on the type of query (text or image),
        it delegates the task to the appropriate handler method.
        
        The session can be terminated by entering 'exit'.
        """
        while True:
            user_input = input("Enter your query or 'exit' to end: ")
            if user_input == 'exit':
                break
            self.session_memory['conversation'].append({"user": user_input})
            self.db_handler(CRUD.INSERT.value, CONVERSATION_HISTORY_TABLE, columns='user_input', values=f'"{user_input}"')
            if "count objects in image" in user_input:
                self.handle_image_query(user_input)
            else:
                self.handle_text_query(user_input)
            print(f"Current Session Memory: {self.session_memory}")

    def process_text(self, user_input):
        """
        Processes a text-based query using the LLAMA language model.
        
        Parameters:
        - user_input (str): The text query from the user.
        
        Returns:
        - str: The generated response from the LLAMA model.
        """
        input_ids = self.llama_tokenizer.encode(user_input, return_tensors="pt")
        output_ids = self.llama_model.generate(input_ids)
        return self.llama_tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    def count_objects(self, image_path):
        """
        Counts the number of objects in an image using the DETR model.
        
        Parameters:
        - image_path (str): The file path for the image to be processed.
        
        Returns:
        - int: The number of objects detected in the image.
        """
        image = Image.open(image_path)
        inputs = self.extractor(images=image, return_tensors="pt")
        outputs = self.detr_model(**inputs)
        target_sizes = torch.tensor([image.size[::-1]])
        results = self.extractor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]
        return len(results["scores"])

# Main block
if __name__ == "__main__":
    """
    Main execution block that initializes the MultimodalAssistant class and starts the interactive session.
    """
    assistant = MultimodalAssistant()
    assistant.session_handler()
