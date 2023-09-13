#!/bin/bash

# Export dependencies to the PATH
export PATH=/usr/bin:$PATH
export PATH=/home/VisuaLlama/.local/bin:$PATH

wait
# Check PATH and Python/Pip
echo "Current PATH: $PATH" | tee -a /home/VisuaLlama/VisuaSetup.log
which python3 | tee -a /home/VisuaLlama/VisuaSetup.log
which pip | tee -a /home/VisuaLlama/VisuaSetup.log

# Install PDM
curl -sSLO https://pdm.fming.dev/install-pdm.py
curl -sSL https://pdm.fming.dev/install-pdm.py.sha256 | shasum -a 256 -c -
python3 install-pdm.py >/dev/null

# Install Ngrok using the specified method
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok -y

wait
# Use nano to edit the example.env file
nano example.env

wait
# Rename the example.env file to .env
mv example.env .env

wait
# Configure Ngrok Tokens
ngrok config add-authtoken $NGROK_AUTHTOKEN
wait
ngrok config add-api-key $NGROK_API_KEY
wait
ngrok config check | tee -a /home/VisuaLlama/VisuaSetup.log

# Install Python packages
pdm install

wait
# Start Python HTTP server in the background
python3 -m http.server 8088& # need to move deployment to correct dir
# move to src/routes/ for the sake of index.html 

# Start Ngrok in the foreground
ngrok http 8088 # need to move deployment to correct dir