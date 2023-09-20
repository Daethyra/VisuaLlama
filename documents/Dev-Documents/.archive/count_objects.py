# Import required libraries
from transformers import DetrImageProcessor, DetrForSegmentation
import torch
from PIL import Image

# Initialize processor and model
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-101-panoptic")
model = DetrForSegmentation.from_pretrained("facebook/detr-resnet-101-panoptic")

# Function to perform object detection and counting based on keyword
def count_objects(image_path, keyword):
    image = Image.open(image_path).convert("RGB")
    
    # Process image and run through the model
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    
    # Post-process the outputs
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    # Initialize counter for the keyword
    count = 0
    for score, label in zip(results["scores"], results["labels"]):
        label = model.config.id2label[label.item()]
        if label.lower() == keyword.lower():
            count += 1
            
    return count

# Example usage
if __name__ == "__main__":
    image_path = "..app/images/*.JPEG"
    keyword = "brown boxes"
    count = count_objects(image_path, keyword)
    print(f"Count of {keyword}: {count}")
