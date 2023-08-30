from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

class Detectron2Manager:
    def __init__(self, config_path, weights_path):
        cfg = get_cfg()
        cfg.merge_from_file(config_path)
        cfg.MODEL.WEIGHTS = weights_path
        self.predictor = DefaultPredictor(cfg)

    def predict(self, image):
        outputs = self.predictor(image)
        return outputs

    def extract_features(self, outputs):
        # Placeholder for feature extraction logic
        return {}