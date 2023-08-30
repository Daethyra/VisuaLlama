# Computer Vision and Conversational Interface Development Roadmap: LLaMA 2 Integration

## 1. Project Overview

### Objective

To build a robust system that combines computer vision using Detectron2 and natural language processing using LLaMA 2 for interactive object counting and description.

### Use Case Example

User wants to count specific types of objects in an image. They upload the image and initiate a conversation with the assistant, specifying their requirements.

## 2. Dynamic Prompt Generation

### 2.1 Context Recognition

- Use the Context Manager Module to manage the conversation history and generate dynamic prompts.
- Implement multi-turn conversations that dynamically generate object classes based on user requirements.

### 2.2 Text Generation

- Integrate LLaMA 2 model using the Llama2Chat Module for text generation.
- Utilize the context from the Context Manager to generate text that aligns with the user's request.

## 3. Object Detection

### 3.1 Detectron2 Integration

- Use the Detectron2 Manager Module for object detection.
- Dynamically generate object classes based on the user's requests and the detected objects.

### 3.2 Image Describer

- Use the Image Describer Module to describe the detected objects.
- Integrate with the Llama2Chat Module to generate conversational descriptions.

## 4. FastAPI Integration

- Use the FastAPI Manager Module to handle API endpoints for image upload and chat functionalities.

## 5. Future Developments

- Implement Google OAuth-based authentication.
- Create TypeScript front-end.
- Implement advanced logging and error handling.
- Add database management for profiles
  - Saved data may include, but is not limited to, per profile: uploaded images, provided natural language inputs
