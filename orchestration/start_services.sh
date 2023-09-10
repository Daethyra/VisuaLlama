#!/bin/bash

# Export dependencies to the PATH
export PATH=/usr/bin:$PATH
export PATH=/home/VisuaLlama/.local/bin:$PATH

# Check PATH and Python/Pip
echo "Current PATH: $PATH" | tee -a /home/VisuaLlama/pysetup.log
which python3 | tee -a /home/VisuaLlama/pysetup.log
which pip | tee -a /home/VisuaLlama/pysetup.log

# Install PDM
curl -sSLO https://pdm.fming.dev/install-pdm.py
curl -sSL https://pdm.fming.dev/install-pdm.py.sha256 | shasum -a 256 -c -
python3 install-pdm.py >/dev/null

# Install Ngrok using the specified method
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok -y

sleep 1
# Configure Ngrok Tokens
ngrok config add-authoken $NGROK_AUTHTOKEN && ngrok config add-api-key $NGROK_API_KEY

# Install Python packages
pdm install

# Start Python HTTP server in the background
python3.8 -m http.server 8088

# Start Ngrok in the foreground
ngrok http 8088 