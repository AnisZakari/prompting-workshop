#!/bin/bash

# Exit on error
set -e

# Function to cleanup background processes
cleanup() {
    echo "Cleaning up..."
    kill $(jobs -p) 2>/dev/null || true
    exit
}

# Set up cleanup on script exit
trap cleanup EXIT

# Change to serve directory
cd serve || { echo "Error: serve directory not found"; exit 1; }

# Start the uvicorn server
echo "Starting uvicorn server..."
uv run uvicorn app.server:app --host 0.0.0.0 --port 8080 &
UVICORN_PID=$!

# Wait a moment for the server to start
sleep 2

# Start ngrok
echo "Starting ngrok..."
uv run ngrok http http://0.0.0.0:8080 &
NGROK_PID=$!

# Wait for both processes
wait $UVICORN_PID $NGROK_PID