# Use an image with CUDA support as base (can be changed for CPU support)
FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu18.04

# Uncomment the following line for CPU support and comment out the above line
# FROM ubuntu:18.04

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update && apt full-upgrade -y && apt install -U -y git wget sudo python3-pip
RUN pip install --user -U pdm && pdm install 

# Create a symbolic link for Python
RUN ln -sv /usr/bin/python3 /usr/bin/python

# Create a non-root user
ARG USER_ID=1000
RUN useradd -m --no-log-init --system --uid ${USER_ID} VisuaLlama -g sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER appuser
WORKDIR /home/appuser

# Install Python dependencies
RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py &&     python3 get-pip.py --user &&     rm get-pip.py
RUN pip install --user -U -r requirements.txt

# Set the working directory and user for subsequent commands
WORKDIR /app
