#!/bin/zsh
# Script to run React app on port 3000, kill process if port is taken

PORT=3000

# Find process using the port and kill it
PID=$(lsof -ti tcp:$PORT)
if [ -n "$PID" ]; then
  echo "Port $PORT is in use by PID $PID. Killing..."
  kill -9 $PID
  sleep 1
fi

# Start the React app
npm start
