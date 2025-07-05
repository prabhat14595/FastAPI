#!/bin/zsh

PORT=8000

# Find and kill the process using the port
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
  echo "Killing process on port $PORT (PID: $PID)..."
  kill -9 $PID
else
  echo "No process found on port $PORT."
fi

# Start FastAPI using the CLI
echo "Starting FastAPI server with 'fastapi run'..."
uvicorn app.main:app --reload --port $PORT --host 0.0.0.0