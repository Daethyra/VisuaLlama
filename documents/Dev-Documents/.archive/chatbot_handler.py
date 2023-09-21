class ModelHandler:
    def __init__(self):
        self.detr_module = DETRops()
        self.prompt = '''
        Act as The Palantir, an AI model trained in \
        object detection and panoptical segmentation. You accurately \
        depict the truth by counting objects for others.
        '''

    def handle_detr(self, image_folder):
        try:
            labeled_segments_json = asyncio.run(self.detr_module.extract_features_async())
            return labeled_segments_json
        except Exception as e:
            return f"Error: {e}"

class ChatbotIntegration:
    def __init__(self):
        self.model_handler = ModelHandler()

    async def handle_image_processing(self, image_folder):
        try:
            labeled_segments_json = await asyncio.to_thread(self.model_handler.handle_detr, image_folder)
            return labeled_segments_json
        except Exception as e:
            return f"Error: {e}"

# Initialize logging
logging.basicConfig(level=logging.INFO)