from fastapi import FastAPI, File, UploadFile
from image_describer import ImageDescriber
from llama2chat import Llama2Chat

app = FastAPI()

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    image_path = f"images/{file.filename}"
    with open(image_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Initialize ImageDescriber and describe image
    image_describer = ImageDescriber('detectron_config.yaml', 'detectron_weights.pth', 'LLaMA_model')
    description = image_describer.describe_image(image_path)

    return {"description": description}

@app.post("/chat/")
def chat(user_input: str):
    # Initialize Llama2Chat and generate text
    llama2chat = Llama2Chat('LLaMA_model')
    response = llama2chat.generate_text(user_input)

    return {"response": response}