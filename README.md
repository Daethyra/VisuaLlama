# VisuaLlama

`A conversational, object-counting AI assistant`

`Project Overview: 9/10/23`

---

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/) [![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://pdm.fming.dev) [![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://pdm.fming.dev) [![PDM](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

#### Current Status

The project is in its initial stages, focusing on a Conversational AI Assistant that assists in counting and distinguishing objects. While the backend framework and basic pipelines are set up, they lack the advanced capabilities required for the project's goals.

#### Goals

1. **Fine-Grained Object Detection** : Use [ViLT](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa) for object detection.
2. **Natural Language Processing** : Use [Llama-2-13b-chat](https://github.com/facebookresearch/llama) for NLP.
3. **Conversational Depth** : Advanced conversational logic to maintain context and ask for additional details.
4. **End-to-End User Flow** : Provide a seamless pipeline for uploading images, descriptions, and continue the conversation with the AI as necessary, with short-term memory enabled.
5. **Publish PyPI package & Docker Image.**

### Modules

#### Backend Modules

1. **detr_detection.py**

   * **Current** : A basic pipeline for object detection and text generation.
   * **To-Do** : Integrate with the UI and AI.

2. **llama_loader.py** : Liason module for VisuaLlama to its LLM counterpart.

#### Planned Development

1. ~~**Deployment files** : Docker, Ngrok~~
2. ~~**Create a Gradio Python module** : Image/text IN; Text OUT.~~
3. **Integrate short-term memory** : State management with 3 most recent messages.
4. **Ngrok Ingress Test** : Confirm that the web application is remotely available.


### Technologies

1. **Dependencies** : Python, PDM(Python Dependency Management)
2. **Object Detection Model** : 
3. **Text Generation Model** : LLaMA-2-13b-chat
4. **Ingress** : Ngrok, Google OAuth

### Steps to Move Forward

1. 

### How to contribute

Please see the [contributing guidelines](CONTRIBUTING.md).

### Citing this repository

Please see the [citations.cff](citations.cff) file.

### How to learn more

Please see the [project documentation](documents).

[![Built-With](https://github-readme-stats.vercel.app/api/top-langs/?username=daethyra&theme=dark)](https://pdm.fming.dev)
