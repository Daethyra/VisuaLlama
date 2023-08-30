import logging
from transformers import AutoModelForCausalLM, AutoTokenizer  # For LLaMA2
from detectron2_manager import Detectron2Manager  # Importing Detectron2 Manager

class Utility:
    def __init__(self):
        self.logger = self.configure_logger("Utility")
        
        # Load LLaMA2 model and tokenizer from local directory
        self.llama2_model = AutoModelForCausalLM.from_pretrained("llama-2-13b-chat")
        self.llama2_tokenizer = AutoTokenizer.from_pretrained("llama-2-13b-chat")
        
        # Initialize Detectron2 Manager
        self.detectron2_manager = Detectron2Manager()
        
    @staticmethod
    def configure_logger(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        return logger
