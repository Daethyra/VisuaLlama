class ContextManager:
    def __init__(self):
        self.history = []
        self.dynamic_classes = []

    def update_history(self, user_input, generated_text):
        self.history.append({"user": user_input, "bot": generated_text})

    def get_history(self):
        return self.history

    def update_dynamic_classes(self, new_classes):
        self.dynamic_classes.extend(new_classes)

    def get_dynamic_classes(self):
        return self.dynamic_classes

    def get_context(self):
        return {
            "history": self.get_history(),
            "dynamic_classes": self.get_dynamic_classes()
        }