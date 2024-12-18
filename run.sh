#!/bin/bash

# Activte the environment
echo "Activating virtual environment..."
source venv/bin/activate

export PYTHONPATH=.

# Execute main script
echo "Running main.py..."
python src/main.py

# Deactivate the environment
echo "Deactivating virtual environment..."
deactivate
