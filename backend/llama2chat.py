from utility import Utility
import logging

class Llama2Chat:
    """A class for generating natural language text using LLaMA 2."""
    
    def __init__(self, utility: Utility):
        self.logger = utility.configure_logger(__name__)
        self.pipeline = utility.text_generation_pipeline
        self.logger.info("Llama2Chat initialized.")
        
    def generate_explanation(self, label_to_count: str, count: int) -> str:
        """Generates a natural language explanation based on the count of label_to_count."""
        try:
            self.logger.info("Generating explanation...")
            prompt = f"How would you explain the presence of {count} {label_to_count}(s) in a room?"
            explanation = self.pipeline(prompt)
            self.logger.info("Explanation generated successfully.")
            return explanation
        except Exception as e:
            self.logger.error(f"An error occurred while generating the explanation: {e}")
            return "An error occurred while generating the explanation."