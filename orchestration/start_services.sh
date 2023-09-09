#!/bin/bash

# Check for necessary environment variables
if [[ -z "$NGROK_AUTH_TOKEN" || -z "$NGROK_API_KEY" ]]; then
  echo "Required NGROK environment variables are not set. Exiting."
  exit 1
fi

# Install PDM into an isolated environment
curl -sSLO https://pdm.fming.dev/install-pdm.py
curl -sSL https://pdm.fming.dev/install-pdm.py.sha256 | shasum -a 256 -c -
python3 install-pdm.py >/dev/null 2>&1

# Install Ngrok using the specified method
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update
sudo apt install ngrok -y >/dev/null 2>&1

# Export environment variables from the .env file
set -o allexport
source /home/VisuaLlama/.env
set +o allexport

# Configure Ngrok Auth Token
ngrok config add-authoken $NGROK_AUTH_TOKEN >/dev/null 2>&1
ngrok config add-api-key $NGROK_API_KEY >/dev/null 2>&1

# Check PATH and Python/Pip
echo "Current PATH: $PATH"
which python3
which pip

# Install PDM
python3 install-pdm.py >/dev/null 2>&1

# Export dependencies to the PATH
export PATH=/usr/bin:$PATH
export PATH=/home/VisuaLlama/.local/bin:$PATH

# Install Python packages
pdm install >/dev/null

# Start Python HTTP server in the background
python3.8 -m http.server 8088

# Start Ngrok in the foreground
ngrok http 8088 