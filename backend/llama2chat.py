from utility import Utility
from context_manager import ContextManager

class Llama2Chat:
    def __init__(self):
        self.utility = Utility("llama-2-13b-chat", "path/to/detectron/config", "path/to/detectron/weights")
        self.context_manager = ContextManager()
        
    def generate_text(self, user_input):
        context = self.context_manager.get_context()
        generated_text = self.utility.llama2_model.generate_text(user_input, context)
        dynamic_classes = self.utility.extract_keywords(generated_text)
        self.context_manager.update_history(user_input, generated_text)
        self.context_manager.update_dynamic_classes(dynamic_classes)
        return generated_text

    def handle_multi_turn(self, user_input):
        # Logic for handling multi-turn conversations
        multi_turn_response = {}  # Placeholder for multi-turn logic
        return multi_turn_response

    def extract_context(self):
        # Logic to extract context for generating more nuanced responses
        context = self.context_manager.get_context()
        return context
