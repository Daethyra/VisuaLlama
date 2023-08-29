from utility import Utility
from fastapi import File, UploadFile
from PIL import Image, ImageDraw
import logging

class ImageDescriber:
    """A class for describing images using object detection."""
    
    def __init__(self, utility: Utility):
        self.logger = utility.configure_logger(__name__)
        self.pipeline = utility.object_detection_pipeline
        self.logger.info("ImageDescriber initialized.")

    def preprocess_image(self, image: Image.Image) -> Image.Image:
        """Preprocesses the given image."""
        self.logger.info("Preprocessing image...")
        image = image.resize((800, 800))
        self.logger.info("Image preprocessed successfully.")
        return image

    def annotate_image(self, image: Image.Image, detections: list) -> Image.Image:
        """Annotates the given image with object detection results."""
        self.logger.info("Annotating image...")
        draw = ImageDraw.Draw(image)
        for detection in detections:
            box = detection['box']
            label = detection['label']
            draw.rectangle(box, outline="red", width=3)
            draw.text((box[0], box[1]), label, fill="red")
        self.logger.info("Image annotated successfully.")
        return image

    def describe_image(self, image: Image.Image, label_to_count: str) -> str:
        """Describes the given image using object detection and count based on label_to_count."""
        try:
            self.logger.info("Describing image...")
            image = self.preprocess_image(image)
            detected_objects = self.pipeline(image)
            count = Utility.count_objects(detected_objects, label_to_count)
            annotated_image = self.annotate_image(image, detected_objects)
            description = f"Detected {count} {label_to_count}(s). Please see the annotated image."
            self.logger.info("Image described successfully.")
            return description, annotated_image
        except Exception as e:
            self.logger.error(f"An error occurred while describing the image: {e}")
            return "An error occurred while processing the image.", None