#!/bin/bash

# Setup DB first manually before running this!
echo "Running Data Pipeline..."
python data_pipeline/fetch_data.py
python data_pipeline/load_to_db.py

# Start API
echo "Starting FastAPI Server..."
uvicorn api.main:app --reload &
sleep 3

# Start UI
echo "Starting UI..."
python ui/app.py
