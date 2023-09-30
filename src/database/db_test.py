# main_controller.py
from database_agent import DatabaseAgent
from models import Conversation, ObjectDetection

def main():
    db_agent = DatabaseAgent()

    # Handle a text query example
    db_agent.db_handler('CREATE', Conversation, session_id=1, user_input="Hello", ai_response="Hi", timestamp="2023-09-29 12:00:00")
    
    # Handle an image query example
    db_agent.db_handler('CREATE', ObjectDetection, session_id=1, image_path="/path/to/image.jpg", bbox_coords="[(0,0), (1,1)]", confidence=0.99, timestamp="2023-09-29 12:05:00")
    
    # Read queries
    print(db_agent.db_handler('READ', Conversation, session_id=1))

if __name__ == '__main__':
    main()
