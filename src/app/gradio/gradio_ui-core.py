# Step 1: Import all necessary libraries and load the DETR model
from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image, ImageDraw
import gradio as gr
import torch

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50-dc5-panoptic")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50-dc5-panoptic")

# Step 2: Define function to perform object detection and counting
def detect_and_count(image, keyword):
    # Process the image and perform detection
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    # let's only keep detections with score > 0.9 (You can also change this threshold)
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    # Initialize counter for the keyword
    count = 0
    
    # Draw boxes on the image and count the instances of the keyword
    draw = ImageDraw.Draw(image)
    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        label = model.config.id2label[label.item()]
        score = round(score.item(), 3)
        
        if label.lower() == keyword.lower():
            count += 1
            draw.rectangle(box, outline="red", width=3)
            draw.text((box[0], box[1]), f"{label} ({score})", fill="red")

    return image, f"Count of {keyword}: {count}"

# Step 3: Create Gradio Interface
image_input = gr.inputs.Image(type="pil", label="Upload Image")
keyword_input = gr.inputs.Textbox(type="str", label="Enter Keyword to Count")

outputs = [
    gr.outputs.Image(type="pil", label="Image with Bounding Boxes"),
    gr.outputs.Textbox(type="str", label="Count")
]

iface = gr.Interface(
    fn=detect_and_count,
    inputs=[image_input, keyword_input],
    outputs=outputs,
    live=True,
    capture_session=True,
)

# Step 4: Launch the Gradio interface
iface.launch()
# need to check gradio docs because this is not working