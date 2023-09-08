#!/bin/bash

# Install PDM into an isolated environment
curl -sSLO https://pdm.fming.dev/install-pdm.py
curl -sSL https://pdm.fming.dev/install-pdm.py.sha256 | shasum -a 256 -c -
python3 install-pdm.py

# Install Ngrok using the specified method
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update
sudo apt install ngrok

# Export environment variables from the .env file
set -o allexport
source /home/VisuaLlama/.env
set +o allexport

# Configure Ngrok Auth Token
ngrok config add-authoken $NGROK_AUTH_TOKEN
ngrok config add-api-key $NGROK_API_KEY

# Execute PDM to install dependencies
pdm install

# Start Python HTTP server in the background
python3.8 -m http.server 8088 &

# Start Ngrok in the foreground
ngrok http 8088
