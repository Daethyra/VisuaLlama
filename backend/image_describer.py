"""This file contains the ImageDescriber class, which is used to describe images using object detection."""
from utility import Utility
from context_manager import ContextManager

class ImageDescriber:
    # Initialize the image describer
    def __init__(self):
        self.utility = Utility("llama-2-13b-chat", "path/to/detectron/config", "path/to/detectron/weights")
        self.context_manager = ContextManager()
        
    # Describe the image
    def describe_image(self, image_path):
        # Object detection using Detectron2
        detections = self.utility.detectron2_predictor(image_path)
        
        # Generate a description based on the detected objects
        detected_objects = detections["instances"].pred_classes
        description = self.utility.llama2_model.generate_text(detected_objects)
        
        # Extract dynamic classes if any
        dynamic_classes = self.utility.extract_keywords(description)
        
        # Update the context manager
        self.context_manager.update_history({"image_path": image_path}, {"description": description})
        self.context_manager.update_dynamic_classes(dynamic_classes)
        
        return description