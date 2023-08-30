""" This file contains the ContextManager class, which is used to store the conversation history and dynamically generated classes.
"""
class ContextManager:
    # Initialize the context manager
    def __init__(self):
        self.conversation_history = []
        self.dynamic_classes = {}
        
    # Enable progressive contextual awareness
    def update_history(self, user_input, system_output):
        self.conversation_history.append({"user": user_input, "system": system_output})
    
    # Enable dynamic class generation    
    def update_dynamic_classes(self, new_classes):
        self.dynamic_classes.update(new_classes)
    
    # Get the context for the next system response    
    def get_context(self):
        return {"history": self.conversation_history, "classes": self.dynamic_classes}
