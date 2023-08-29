from transformers import pipeline
import logging
from datetime import datetime

class Utility:
    """A class for loading pipelines using the transformers library and providing methods for their implementation."""
    
    def __init__(self):
        self.logger = self.configure_logger("Utility")
        self.text_generation_pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")
        self.object_detection_pipeline = pipeline("object-detection", model="facebook/detr-resnet-50")
        self.logger.info("Utility initialized.")
        
    @staticmethod
    def configure_logger(name):
        """Configures a logger for a given module name."""
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(name)
        log_filename = f"{name}_{datetime.now().strftime('%m-%d-%Y_%H-%M')}.log"
        handler = logging.FileHandler(log_filename)
        logger.addHandler(handler)
        return logger
    
    def generate_text(self, prompt, parameters=None):
        """Generates text based on a prompt."""
        if parameters is None:
            parameters = {}
        return self.text_generation_pipeline(prompt, **parameters)[0]
    
    def detect_objects(self, image):
        """Detects objects in an image."""
        return self.object_detection_pipeline(image)
        
    def count_objects(self, detected_objects: list, label: str) -> int:
        """Counts the number of objects with a specific label in the detected objects."""
        count = 0
        for obj in detected_objects:
            if obj['label'] == label:
                count += 1
        return count