# The default base image is 'ubuntu:18.04' which defaults to CPU processing and was chosen for backwards compatibility.
#
# If you want to use GPU then uncomment the appropriate lines, both here and in 'orchestration/compose.yml'.
# Only change this file if you know what you are doing.
#
# | ---------------------------------- |
# ---- {Base Build Stage} ----
# Use an image with CUDA support as base (can be changed for CPU support)
#FROM ubuntu:latest AS base
FROM ubuntu:18.04 AS base

# Uncomment the following line for GPU support and comment out the above line
#FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu18.04 AS base

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=noninteractive
# | ---------------------------------- |
# ---- {Dependencies Stage} ----
FROM base AS dependencies
# Copy the necessary folders and files into the image
COPY src/ /home/VisuaLlama/src/
COPY pyproject.toml /home/VisuaLlama/
COPY .env /home/VisuaLlama/
COPY orchestration/start_services.sh /home/VisuaLlama/
RUN chmod +x /home/VisuaLlama/start_services.sh
# Install basic image dependencies
RUN apt update && \
    apt full-upgrade -y && \
    apt install -y git wget curl sudo nano 
# Install Ngrok from the official repository via apt
RUN  curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list && apt update && \
    apt install ngrok
# Install PDM (Python Development Master) from PyPI  (https://pdm.fming.dev/)
RUN python3.8 -m pip install pdm pdm-backend
# Install Python dependencies from pyproject.toml using pdm install
RUN pdm venv create && \
    pdm install
# | ---------------------------------- |
# ---- {Final Stage} ----
FROM dependencies AS final
ARG USER_ID=1000
# Create a non-root user and set permissions
RUN useradd -m --no-log-init --system --uid ${USER_ID} VisuaLlama -g sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
# Change ownership of the home directory
RUN chown -R VisuaLlama:sudo /home/VisuaLlama
# Set user and working directory
USER VisuaLlama
WORKDIR /home/VisuaLlama

RUN apt update && \
    apt install -y python3.8 python3-pip python3.8-venv && \
    python3.8 -m pip install --upgrade pip
# Run the Bash script to start the Python HTTP server and Ngrok
CMD ["/bin/bash", "/home/VisuaLlama/start_services.sh"]