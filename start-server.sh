#!/bin/bash

# Activate your virtual environment
source pw_env/bin/activate

# Set Flask app environment variable
export FLASK_APP=website.py

# Run Flask server in the background
flask run &

# Wait a few seconds for the server to start
sleep 2

# Open the webpage in your default browser
xdg-open http://127.0.0.1:5000/