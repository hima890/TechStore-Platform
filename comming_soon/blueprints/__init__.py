from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from config import ProConfig, TestConfig

# Load environment variables from .env file
load_dotenv("../.env")

# Determine which config class to use
config_name = os.getenv('FLASK_CONFIG', 'config.ProConfig')  # Default to Config if not set

print(os.getenv('SECRET_KEY')
#!/usr/bin/env bash
# A Bash script that generates a MySQL dump and creates a compressed archive out of it.

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <mysql-root-password>"
    exit 1
fi

MYSQL_ROOT_PASSWORD=$1
BACKUP_DIR="$(pwd)"

# Create a timestamp for the backup file
TIMESTAMP=$(date +"%d-%m-%Y")

# Create MySQL dump and check if mysqldump was successful
if ! mysqldump -u root -p"${MYSQL_ROOT_PASSWORD}" --all-databases > backup.sql; then
    echo "mysqldump failed"
    exit 1
fi

# Create a compressed archive
if ! tar -czvf "${BACKUP_DIR}/${TIMESTAMP}.tar.gz" backup.sql; then
    echo "tar compression failed"
    exit 1
fi

# Remove the SQL dump file to save space
if ! rm backup.sql; then
    echo "Failed to remove backup.sql"
    exit 1
fi

# Create the SQLAlchemy object
db = SQLAlchemy()

def create_app(config_class=config_name):
    """
    This function is used to create the Flask app and register the blueprints.
    
    Return: The Flask app.
    """
    # Initialize the app
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object(config_class)

    # Initialize the SQLAlchemy object
    db.init_app(app)

    # Register the blueprints
    from blueprints.landingPage.routes.landingPage_route import landingPage
    app.register_blueprint(landingPage)

    # Create the database
    with app.app_context():
        import models
        db.create_all()

    return app
