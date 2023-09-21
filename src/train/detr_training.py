from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image, ImageDraw
import os
import torchvision.transforms as T

class DETRFineTuner:
    def __init__(self, model_name="facebook/detr-resnet-50", images_path="images/"):
        """
        Initialize the DETRFineTuner class.
        
        Parameters:
        - model_name (str): The name of the pre-trained DETR model to use.
        - images_path (str): The path to the directory containing images for fine-tuning.
        """
        self.model_name = model_name
        self.images_path = images_path
        self.processor = DetrImageProcessor.from_pretrained(model_name)
        self.model = DetrForObjectDetection.from_pretrained(model_name)

    def load_images(self):
        """
        Load images from the specified directory.
        
        Returns:
        - images (list): A list of loaded images.
        """
        images = []
        for filename in os.listdir(self.images_path):
            image_path = os.path.join(self.images_path, filename)
            image = Image.open(image_path)
            images.append(image)
        return images

    def fine_tune(self, images, epochs=1, lr=0.001):
        """
        Fine-tune the DETR model on the provided images.
        
        Parameters:
        - images (list): A list of images for fine-tuning.
        - epochs (int): Number of epochs for fine-tuning.
        - lr (float): Learning rate for the optimizer.
        """
        # Prepare data
        inputs = self.processor(images, return_tensors="pt")
        target_sizes = torch.tensor([image.size[::-1] for image in images])

        # Prepare model and optimizer
        self.model.train()
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=lr)

        # Fine-tuning loop
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = self.model(**inputs, target_sizes=target_sizes)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")

    def save_model(self, save_path):
        """
        Save the fine-tuned model.
        
        Parameters:
        - save_path (str): The path to save the fine-tuned model.
        """
        self.model.save_pretrained(save_path)
        
    def run(self, epochs=1, lr=0.001, save_path="fine_tuned_detr"):
        """
        Run the fine-tuning process end-to-end.
        
        Parameters:
        - epochs (int): Number of epochs for fine-tuning.
        - lr (float): Learning rate for the optimizer.
        - save_path (str): The path to save the fine-tuned model.
        """
        images = self.load_images()
        self.fine_tune(images, epochs=epochs, lr=lr)
        self.save_model(save_path)