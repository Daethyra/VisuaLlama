"Manage all Detectron2, non-specific, reusable code here. "
import detectron2
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor

class Detectron2Manager:
    def __init__(self):
        self.cfg = self.configure_detectron2()
        self.model = DefaultPredictor(self.cfg)

    @staticmethod
    def configure_detectron2():
        cfg = get_cfg()
        cfg.merge_from_file("path/to/config/file.yaml")
        cfg.MODEL.WEIGHTS = "path/to/model/weights"
        cfg.MODEL.DEVICE = "cpu"  # or "cuda"
        return cfg

    def detect_objects(self, image):
        outputs = self.model(image)
        return outputs
