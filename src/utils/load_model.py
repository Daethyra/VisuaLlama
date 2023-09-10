from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
import asyncio


class LoadVilt():
    """Class for loading ViLT models."""
    def __init__(self):
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        self.model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    async def get_top_answer(self, image, text):
        # prepare inputs
        encoding = self.processor(image, text, return_tensors="pt")

        # forward pass
        outputs = self.model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()

        return idx

async def main():
    vilt = LoadVilt()
    tasks = []
    for image, text in batch:
        task = asyncio.create_task(vilt.get_top_answer(image, text))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results