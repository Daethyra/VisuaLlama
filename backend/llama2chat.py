from utility import Utility
from context_manager import ContextManager

class Llama2Chat:
    def __init__(self, model_path):
        self.utility = Utility(model_path)
        self.context_manager = ContextManager()

    def generate_text(self, user_input):
        context = self.context_manager.get_context()
        generated_text = self.utility.generate_text(user_input, context)

        # Update history and context
        self.context_manager.update_history(user_input, generated_text)

        # Placeholder for dynamic class generation logic
        return generated_text