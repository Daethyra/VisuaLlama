""" This module provides a class for centralizing prompting/generation \
    via `generation.py` found in the 'meta' subdir.
    
    The class wraps content with proper special tags before \
    passing it to `generation.py` for generation.
    """
from meta.generation import Llama

# Encode special tags
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"

SPECIAL_TAGS = [B_INST, E_INST, "<<SYS>>", "<</SYS>>"]
UNSAFE_ERROR = "Error: special tags are not allowed as part of the prompt."
# ----- #

# Function to wrap content with special tags
def wrap_with_special_tags(content, tag_type):
    if tag_type == 'INST':
        return f"{B_INST}{content}{E_INST}"
    elif tag_type == 'SYS':
        return f"{B_SYS}{content}{E_SYS}"
    else:
        return f"{UNSAFE_ERROR}"

# Create a class for generating natural language from Llama-2-13b-chat
class MetaSource:
    # Initialize the Llama-2-13b-chat model
    def __init__(self):
        self.llama = Llama()
    
    # Generate natural language from Llama-2-13b-chat
    async def generate(self, prompt):
        try:
            # Check if prompt contains special tags
            if any(tag in prompt for tag in SPECIAL_TAGS):
                return UNSAFE_ERROR
            # Generate natural language from Llama-2-13b-chat
            generated_text = await self.llama.generate(prompt)
            # Return the generated text
            return generated_text
        except Exception as e:
            return str(e)
    
    # Create a cache for stateful memory
    def create_cache(self):
        self.cache = {
            'prompts': [],
            'responses': []
        }
        
        self.cache['prompts'].append(wrap_with_special_tags("", 'INST'))
        self.cache['responses'].append(wrap_with_special_tags("", 'SYS'))
        
        # Limit the cache size to 3 messages
        if len(self.cache['prompts']) > 3:
            self.cache['prompts'] = self.cache['prompts'][-3:]
            self.cache['responses'] = self.cache['responses'][-3:]
