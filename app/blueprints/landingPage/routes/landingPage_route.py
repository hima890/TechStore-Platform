from flask import Blueprint, render_template

landingPage = Blueprint('landingPage', __name__,
                        static_folder='../static',
                        template_folder='../templates')


@landingPage.route('/')
@landingPage.route('/home')
def home():
    return render_template('index.html')
