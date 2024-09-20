#!/usr/bin/python3
""" Flask Application """
from app.config import config  # Import the config dictionary from your config.py
from app import create_app

# Create the Flask app instance
app = create_app(config['testing'])

@app.route('/')
def home():
    return 'Welcome to the TechStore API!'

# Run the app
if __name__ == '__main__':
    app.run(port=5001)
