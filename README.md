# VisuaLlama

`A conversational, object-counting AI assistant`

`Project Overview: 8/28/23`

---

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

#### Current Status

The project is in its initial stages, focusing on a Conversational AI Assistant that assists in counting and distinguishing objects. While the backend framework and basic pipelines are set up, they lack the advanced capabilities required for the project's goals.

#### Goals

1. **Fine-Grained Object Detection** : To be achieved by implementing RCNN/Mask RCNN. (Replace CLIP)
2. **Conversational Depth** : Advanced conversational logic to maintain context and ask for additional details.
3. **End-to-End User Flow** : Users should be able to upload an image and get a natural language explanation.

#### Future Development

1. **Front-End** : TypeScript interface for user interaction.
2. **Account Management** : Implementation of Google OAuth.

### Modules

#### Backend Modules

1. **Utility.py**
   * **Current** : Contains pipelines for text generation and object detection, but not fine-grained.
   * **To-Do** : Integrate RCNN/Mask RCNN.
2. **ImageDescriber.py** -> `image_processing.py`
   * **Current** : Capable of basic image resizing and object annotation.
   * **To-Do** : Integrate RCNN/Mask RCNN for detailed object detection. Add logic for categorizing similar object types.
3. **Llama2Chat.py** -> `conversation.py`
   * **Current** : Basic text generation. No adaptive responses or state management.
   * **To-Do** : Implement context-aware conversational logic and state management. Enable data ingestion during runtime. Enable data reception from Mask-RCNN.

#### Front-End Functionalities (Planned)

1. **Conversation Chat Display** : To display the back-and-forth between the user and AI.
2. **Interactive Functionality** : To allow users to assist the AI in identification tasks.
3. **State Management** : Real-time updates of the AI's state.
4. **Image Upload** : Functionality for users to upload images.
5. **User Accounts** : Google OAuth for user access.

### Technical Requirements

1. **Back-End** : Python, FastAPI
2. **Object Detection Model** : Intending to use RCNN/Mask RCNN
3. **Text Generation Model** : LLaMA 2
4. **Front-End** : TypeScript (to be developed)

### Steps to Move Forward

1. **Object Detection** : Research and implement RCNN/Mask RCNN.
2. **Conversational Logic** : Enhance `Llama2Chat.py` for state management and improved dialog.
3. **Front-End Development** : Build the TypeScript interface with planned functionalities.
4. **Account Management** : Implement Google OAuth.
5. **Testing** : Conduct thorough testing of each component.

### How to learn more

Please see the [progressive project documentation](documents/)
