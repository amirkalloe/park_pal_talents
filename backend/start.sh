#! /usr/bin/env bash

# Start the backend server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000