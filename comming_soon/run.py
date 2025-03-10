"""
This is the entry point of the application.
"""
from blueprints import create_app

#  Create the app
app =  create_app()

# Run the app
if __name__ == "__main__":
    app.run(debug=True,
            port=5003)
