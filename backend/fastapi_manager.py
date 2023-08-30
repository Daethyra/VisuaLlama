"""FastAPI routes for the VisuaLlama backend."""

from fastapi import FastAPI, UploadFile, File
from utility import Utility
from context_manager import ContextManager
from detectron2_manager import Detectron2Manager
from llama2chat import Llama2Chat
from image_describer import ImageDescriber

app = FastAPI()

@app.post("/upload_image/")
async def upload_image(image: UploadFile = File(...)):
    image_describer = ImageDescriber()
    description = image_describer.describe_image(image.filename)
    return {"description": description}

@app.post("/chat/")
async def chat(user_input: str):
    llama2chat = Llama2Chat()
    generated_text = llama2chat.generate_text(user_input)
    return {"response": generated_text}
