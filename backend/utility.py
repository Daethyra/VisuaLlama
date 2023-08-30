import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor

class Utility:
    def __init__(self, model_path, detectron_config, detectron_weights):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)

        cfg = get_cfg()
        cfg.merge_from_file(detectron_config)
        cfg.MODEL.WEIGHTS = detectron_weights
        self.detectron2_predictor = DefaultPredictor(cfg)
        
    def generate_text(self, text, context=None):
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        with torch.no_grad():
            output = self.model.generate(input_ids)
        decoded = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return decoded

    def detectron2_predictor(self, image_path):
        # Placeholder for Detectron2 prediction logic
        return {}

    def extract_keywords(self, text):
        # Placeholder for keyword extraction logic
        return []

    def log_error(self, error_message):
        # Placeholder for logging errors
        pass