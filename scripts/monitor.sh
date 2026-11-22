#!/bin/bash

URL="http://localhost:8080/health"
LOG_FILE="$HOME/PROJECT/mini-ai-infras/health.log"
TIMESTAMP=$(date "+%Y-%m-%d %H-%M-%S")

RESPONSE=$(curl -sf "$URL")

if [ $? -eq 0 ]; then
    echo "[$TIMESTAMP] OK - $RESPONSE" >> "$LOG_FILE"
else
    echo "[$TIMESTAMP] ERROR: Service down!" >> "$LOG_FILE"
fi