#!/bin/bash

# Configure Ngrok Auth Token
ngrok config add-authoken $NGROK_AUTH_TOKEN

# Start Python HTTP server in the background
python3.8 -m http.server 8088 &

# Start Ngrok in the foreground
ngrok http 8088
