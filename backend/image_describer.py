from detectron2_manager import Detectron2Manager
from utility import Utility

class ImageDescriber:
    def __init__(self, detectron_config, detectron_weights, model_path):
        self.detectron_manager = Detectron2Manager(detectron_config, detectron_weights)
        self.utility = Utility(model_path)

    def describe_image(self, image_path):
        # Detect objects using Detectron2
        outputs = self.detectron_manager.predict(image_path)
        features = self.detectron_manager.extract_features(outputs)

        # Generate description using LLaMA2
        description = self.utility.generate_text("Describe this image.", context=features)

        return description