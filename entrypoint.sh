#!/bin/sh

# Start Supervisord in the background
supervisord -c /etc/supervisord.conf &

# Start FastAPI in the foreground
uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
