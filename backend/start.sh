#! /usr/bin/env bash

# Run migration
alembic -c alembic/alembic.ini upgrade head
# Start the backend server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000