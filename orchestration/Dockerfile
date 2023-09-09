# The default base image is 'ubuntu:18.04' which defaults to CPU processing and was chosen for backwards compatibility.
#
# If you want to use GPU then uncomment the appropriate lines, both here and in 'orchestration/compose.yml'.
# Only change this file if you know what you are doing.
#
# | ---------------------------------- |
# ---- {Base Build Stage} ----
# Use an image with CUDA support as base (can be changed for CPU support)
FROM nvidia/cuda:12.0.1-cudnn8-devel-ubuntu18.04 AS base

# Uncomment the following line for CPU support and comment out the above line
#FROM ubuntu:18.04 AS base

# Set environment variables to non-interactive and timezone
ENV DEBIAN_FRONTEND=noninteractive TZ=America/Los_Angeles

# Install system dependencies
RUN apt update && \
    apt install -y wget curl nano software-properties-common sudo
# Create a non-root user and set permissions
RUN useradd -m --no-log-init --system VisuaLlama -g sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# ---- {Dependencies Stage} ----
FROM base AS dependencies
USER VisuaLlama
WORKDIR /home/VisuaLlama

# Copy only necessary files to make use of Docker's caching mechanism
COPY pyproject.toml .
COPY .env .

# Switch back to root for package installations
USER root
WORKDIR /home/VisuaLlama
# Consolidate RUN commands and install only essential packages
RUN apt-add-repository ppa:deadsnakes/ppa -y && \
    apt update -y && \
    apt full-upgrade -y && \
    apt install -y python3.8 python3.8-venv

# ---- {Final Stage} ----
FROM dependencies AS final
USER VisuaLlama
ARG USER_ID=1000

# Install pip at the user level
RUN sudo apt install -y python3-pip python3-venv && \
    python3.8 -m pip install --upgrade pip && \
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Copy the rest of the files into the image
COPY src/ ./src/
COPY orchestration/start_services.sh ./start_services.sh
RUN sudo chmod +x ./start_services.sh && \
    sudo apt autoremove -y

# Run the Bash script to start the Python HTTP server and Ngrok
CMD ["/bin/bash", "/home/VisuaLlama/start_services.sh"]
