"""A versatile backend module for Visual Question Answering using ViLT."""

import tensorflow as tf
from transformers import ViltProcessor, TFAutoModelForQuestionAnswering
from PIL import Image
import logging
import os
from utils.load_model import LoadVilt

class VILTChatbotModule:
    """Class for handling Visual Question Answering using ViLT."""

    def __init__(self, model_name="dandelin/vilt-b32-finetuned-vqa"):
        """
        Initialize the VILTChatbotModule with pretrained models.

        Parameters:
        - model_name (str): The name of the pretrained model to use.
        """
        try:
            self.processor = ViltProcessor.from_pretrained(model_name)
            self.model = TFAutoModelForQuestionAnswering.from_pretrained(model_name)
        except Exception as e:
            logging.error(f"Error in loading pretrained models: {str(e)}")
            raise

    def load_image(self, image_input):
        """
        Load an image from a local path or PIL Image object.

        Parameters:
        - image_input (str or PIL.Image.Image): The input image.

        Returns:
        - PIL.Image.Image or None: The loaded image or None if an error occurs.
        """
        try:
            if isinstance(image_input, str) and os.path.exists(image_input):
                image = Image.open(image_input)
            elif isinstance(image_input, Image.Image):
                image = image_input
            else:
                raise ValueError("Invalid image input. Provide either a local path or a PIL Image object.")
            
            return image
        except Exception as e:
            logging.error(f"Error in loading image: {str(e)}")
            return None

    def predict_answer(self, image_input, text):
        """
        Predict an answer for a visual question based on an image and text.

        Parameters:
        - image_input (str or PIL.Image.Image): The input image.
        - text (str): The question or text description.

        Returns:
        - str or None: The predicted answer or None if an error occurs.
        """
        try:
            image = self.load_image(image_input)
            if image is None:
                raise ValueError("Failed to load image.")

            encoding = self.processor(image, text, return_tensors="tf")
            outputs = self.model(encoding)
            logits = outputs.logits
            idx = tf.math.argmax(logits, axis=-1).numpy()[0]
            return self.model.config.id2label[idx]
        except Exception as e:
            logging.error(f"Error in prediction: {str(e)}")
            return None

def get_prediction(image_input, text):
    """
    Get the predicted answer for a visual question.

    Parameters:
    - image_input (str or PIL.Image.Image): The input image.
    - text (str): The question or text description.

    Returns:
    - dict: A dictionary containing the predicted answer or an error message.
    """
    try:
        vilt_module = VILTChatbotModule()
        answer = vilt_module.predict_answer(image_input, text)
        if answer:
            return {"Predicted answer": answer}
        else:
            return {"error": "An error occurred during prediction."}
    except Exception as e:
        return {"error": str(e)}
