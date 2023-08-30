#!/bin/bash

# Install Python dependencies
echo "Installing Python dependencies..."
python -m pip install fastapi torch transformers

# Install Detectron2 from source
echo "Installing Detectron2..."
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'

# Build and run Docker containers (you can customize these commands according to your needs)
echo "Building Docker image..."
docker build --build-arg USER_ID=$UID -t detectron2:v0 .

echo "Running Docker container..."
docker run --gpus all -it --shm-size=8gb --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --name=detectron2 detectron2:v0

# Other system-specific setups can go here
