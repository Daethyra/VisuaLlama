# VisuaLlama

`A conversational, object-counting AI assistant`

`Project Overview: 9/10/23`

---

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/) [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://pdm.fming.dev) [![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://pdm.fming.dev) [![PDM](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

#### Current Status

The project is in its initial stages, focusing on a Conversational AI Assistant that assists in counting and distinguishing objects. While the backend framework and basic pipelines are set up, they lack the advanced capabilities required for the project's goals.

#### Goals

1. **Fine-Grained Object Detection** : Use [ViLT](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa) for object detection.
2. **Natural Language Processing** : Use Llama-2-13b-chat for NLP.
3. **Conversational Depth** : Advanced conversational logic to maintain context and ask for additional details.
4. **End-to-End User Flow** : Provide a seamless pipeline for uploading images, descriptions, and continue the conversation with the AI as necessary, with short-term memory enabled.
5. **Publish PyPI package & Docker Image.**

### Modules

#### Backend Modules

1. **vilt_power.py**

   * **Current** : A basic pipeline for object detection and text generation.
   * **To-Do** : Integrate with the UI and AI.
2. **llama_loader.py** : Liason module for VisuaLlama to its LLM counterpart.

#### Planned Development

1. ~~**Deployment files** : Docker, Ngrok~~
2. ~~**Create a Gradio Python module** : Image/text IN; Text OUT.~~
3. **Initialize Submodule** : Using, Git, initialize the official Llama repository as a submodule.
4. **Integrate short-term memory** : State management by caching 6 chat messages.
5. **Ngrok Ingress Test** : Confirm that the web application is remotely available.
6. **Initialize Llama as submodule** : Using, Git, initialize the official Llama repository as a submodule.

### Technologies

1. **Setup** : Python, PDM(Python Dependency Management)
2. **Object Detection Model** : ViLT
3. **Text Generation Model** : LLaMA-2-13b-chat
4. **Ingress** : Ngrok, Google OAuth

### Steps to Move Forward

1. **Object Detection Testing** : Test ViLT for object detection with its testsuite.
2. **Test LLaMA generation functions** : Load the local model with `llama_loader.py` in `LLMhandlers/`; test the pipeline for text generation.
3. **ViLT integration with Gradio and Testing** : Test the Gradio interface by integrating `vilt_power.py` module. Ensure the base UX aligns with the project's end goals.

### How to contribute

Please see the [contributing guidelines](CONTRIBUTING.md).

### Citation

Please see the [citations.cff](citations.cff) file.

### How to learn more

Please see the [project documentation](documents).

[![Built-With](https://github-readme-stats.vercel.app/api/top-langs/?username=daethyra&theme=synthwave)](https://pdm.fming.dev)
