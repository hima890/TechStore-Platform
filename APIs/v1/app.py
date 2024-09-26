#!/usr/bin/python3
""" Flask Application """
from app import create_app

# Create the Flask app instance
run = create_app()

# Run the app
if __name__ == '__main__':
    run.run(port=5001)

