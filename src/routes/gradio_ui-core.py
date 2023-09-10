""" This file contains the Gradio interface for the VQA model. """
# Full path: /src/routes/gradio_ui-core.py
import gradio as gr

#def vqa_function(question, image):
    # Your VQA logic here
    # For example, return an answer based on the question and image.
    #return "Sample Answer"

# Define Gradio interface
iface = gr.Interface(
    fn=vqa_function, 
    inputs=["text", "image"], 
    outputs="text"
)

# Launch the Gradio interface
iface.launch()
