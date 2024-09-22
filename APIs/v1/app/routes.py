from flask import Blueprint, render_template

# Create a Blueprint for routes
main = Blueprint('main', __name__)

# Landing page route
@main.route('/')
def landing_page():
    return render_template('landing.html')

# API home route
@main.route('/api')
def home():
    return 'Welcome to the TechStore API!'
