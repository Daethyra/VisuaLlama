# Use an image with CUDA support as base (can be changed for CPU support)
FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu18.04

# Uncomment the following line for CPU support and comment out the above line
# FROM ubuntu:18.04

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y     python3-opencv ca-certificates python3-dev git wget sudo ninja-build

# Create a symbolic link for Python
RUN ln -sv /usr/bin/python3 /usr/bin/python

# Create a non-root user
ARG USER_ID=1000
RUN useradd -m --no-log-init --system --uid ${USER_ID} appuser -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER appuser
WORKDIR /home/appuser

# Install Python dependencies
RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py &&     python3 get-pip.py --user &&     rm get-pip.py
RUN pip install --user fastapi torch transformers 'git+https://github.com/facebookresearch/detectron2.git'

# Set the working directory and user for subsequent commands
WORKDIR /app
