from collections import Counter
from transformers import AutoModelForCausalLM, AutoTokenizer
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import re

class Utility:
    def __init__(self):
        # Load the LLaMA2 model and tokenizer
        self.llama2_model = AutoModelForCausalLM.from_pretrained("llama-2-13b-chat")
        self.llama2_tokenizer = AutoTokenizer.from_pretrained("llama-2-13b-chat")
        
        # Load the Detectron2 model
        cfg = get_cfg()
        cfg.merge_from_file("path/to/config/file.yaml")
        cfg.MODEL.WEIGHTS = "path/to/weights/file.pth"
        self.detectron2_predictor = DefaultPredictor(cfg)
        
    def extract_keywords(self, text, top_n=5):
        """Extract top_n keywords from a given text based on frequency."""
        words = re.findall(r'\\w+', text.lower())
        counter = Counter(words)
        common_words = counter.most_common(top_n)
        return [word[0] for word in common_words]
