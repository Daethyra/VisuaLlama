from utility import Utility

class Detectron2Manager:
    def __init__(self):
        self.utility = Utility("llama-2-13b-chat", "path/to/detectron/config", "path/to/detectron/weights")
        
    def detect_objects(self, image_path):
        # Object detection using Detectron2
        detections = self.utility.detectron2_predictor(image_path)
        detected_objects = detections["instances"].pred_classes
        return detected_objects
