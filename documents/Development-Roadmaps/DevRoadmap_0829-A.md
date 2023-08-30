# VisuaLlama Development Roadmap

## Overview

The VisuaLlama project aims to create a Conversational AI Assistant capable of counting and distinguishing objects in uploaded images. This document outlines the development roadmap to guide the project from its current state to a fully functional application.

---

## Modules

### 1. Utility Module

#### Goals

- Refactor to support fine-grained object detection using Detectron2.
- Enhance the text generation capabilities using LLaMA2.

#### Tasks

1. Finalize the utility class for production use.
2. Integrate advanced error handling and logging.

### 2. Context Manager Module

#### Goals

- Manage the context and state of the conversation.
- Enable dynamic class creation.

#### Tasks

1. Implement methods for updating and retrieving conversation history.
2. Add functionalities for context extraction.

### 3. Detectron2 Manager Module

#### Goals

- Object detection using Detectron2.
- Feature extraction from detected objects.

#### Tasks

1. Implement object detection methods.
2. Add logic for feature extraction and processing.

### 4. Image Describer Module

#### Goals

- Describe objects in images using natural language.
- Integrate with Detectron2 and LLaMA2.

#### Tasks

1. Implement methods for generating text-based image descriptions.
2. Add logic for dynamic class creation based on text descriptions.

### 5. Llama2Chat Module

#### Goals

- State management and context-aware text generation.
- Multi-turn conversation capabilities.

#### Tasks

1. Add methods for multi-turn conversations.
2. Implement context extraction logic.

### 6. FastAPI Manager Module

#### Goals

- Create FastAPI endpoints for image upload and chat functionalities.
- Integrate all other modules.

#### Tasks

1. Implement FastAPI endpoints for user interactions.
2. Add error handling and request validation.

---

## Additional Components

### Front-End Development

- Develop the TypeScript interface with chat display, image upload, and user accounts.

### User Authentication

- Implement Google OAuth for user authentication.

### Testing Framework

- Implement unit and integration tests for all modules.

---

## Timeline

1. **Week 1-2**: Finalize Utility and Context Manager Modules.
2. **Week 3-4**: Complete Detectron2 Manager and Image Describer Modules.
3. **Week 5-6**: Finish Llama2Chat and FastAPI Manager Modules.
4. **Week 7-8**: Front-End Development and User Authentication.
5. **Week 9-10**: Comprehensive Testing and Deployment.

---

## Conclusion

This roadmap provides a structured plan for developing the VisuaLlama project. By following these guidelines, we aim to build a robust and functional Conversational AI Assistant.
