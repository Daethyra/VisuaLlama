# VisuaLlama

`A conversational, object-counting AI assistant`

`Project Overview: 9/5/23`

---

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

#### Current Status

The project is in its initial stages, focusing on a Conversational AI Assistant that assists in counting and distinguishing objects. While the backend framework and basic pipelines are set up, they lack the advanced capabilities required for the project's goals.

#### Goals

1. **Fine-Grained Object Detection** : Use [ViLT](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa) for object detection.
2. **Conversational Depth** : Advanced conversational logic to maintain context and ask for additional details.
3. **End-to-End User Flow** : Users should be able to upload an image, describe their issue in natural language, and get a natural language response.

#### Future Development

1. **User Interface** : Gradio
2. **Account Management** : Google OAuth
3. **Deployment** : Docker, Ngrok

### Modules

#### Backend Modules

1. **vilt_power.py**

   * **Current** : A basic pipeline for object detection and text generation.
   * **To-Do** : 

#### Front-End Functionalities (Planned)

1. **Conversation Chat Display** : To display the back-and-forth between the user and AI.
2. **Interactive Functionality** : To allow users to assist the AI in identification tasks.
3. **State Management** : Real-time updates of the AI's state.
4. **Image Upload** : Functionality for users to upload images.
5. **User Accounts** : Google OAuth for user access.

### Technical Requirements

1. **Back-End** : Python, FastAPI
2. **Object Detection Model** : ViLT 
3. **Text Generation Model** : LLaMA 2

### Steps to Move Forward

1. **Object Detection Testing** : Test ViLT for object detection.
2. **User Interface** : Create Gradio module
3. **Gradio Test** : Test the Gradio interface with the `vilt_power.py` module. Ensure the UX aligns with the project goals.
4. **Initialize Llama as a submodule** : Load the local model with a Python module in `models/`. Create a pipeline for text generation.

### How to learn more

Please see the [progressive project documentation](documents/).
