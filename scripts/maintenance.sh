#!/bin/bash

# Script for basic code maintenance

# Install dependencies
if [ -f requirements.txt ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Run tests
if [ -d tests ]; then
    echo "Running tests..."
    pytest tests/
fi

# Clean up
echo "Cleaning up..."
rm -rf __pycache__

echo "Maintenance complete!"
