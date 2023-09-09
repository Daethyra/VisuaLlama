""" This module centralizes the handling of modules created by Meta. """

# Local imports
from vilt_power import VILTChatbotModule
from meta import Llama, ModelArgs, Transformer, Tokenizer

""" NEEDS OVERHAUL AND USAGE TO TEST VILT """
class LlamaLoader:
    def __init__(self):
        self.vilt_module = VILTChatbotModule()
        self.zero_shot_prompt = "You are an AI model trained to assist in counting and distinguishing objects."
        self.llama_model = Llama(ModelArgs())
        self.llama_tokenizer = Tokenizer()
        self.llama_generator = Transformer()

    def process_user_input(self, input_text):
        # Use Meta's Llama tokenizer to process user input
        parsed_input = self.llama_tokenizer.tokenize(input_text)
        
        return parsed_input

    def generate_vqa_input(self, user_image):
        # Use Meta's Llama model to generate VQA input parameters
        vqa_input = self.llama_model.generate_vqa_input(user_image)
        
        return vqa_input

    def process_vqa_output(self, vqa_output):
        # Use Meta's Llama generator to process VQA output
        processed_output = self.llama_generator.process_vqa_output(vqa_output)
        
        return processed_output

    def process_user_request_specifics(self, input_text):
        # Use Meta's Llama model to capture user specifics
        user_specifics = self.llama_model.process_user_request_specifics(input_text)
        
        return user_specifics
