#!/usr/bin/python3
""" Flask Application """
from app import create_app

# Create the Flask app instance
app = create_app()

@app.route('/')
def home():
    return 'Welcome to the TechStore API!'

# Run the app
if __name__ == '__main__':
    app.run(port=5001)
