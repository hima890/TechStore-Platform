from flask import Blueprint, render_template, request, redirect, url_for


landingPage = Blueprint('landingPage', __name__,
                        static_folder='../static',
                        template_folder='../templates',
                        static_url_path='/static/landingPage')


@landingPage.route('/')
@landingPage.route('/home')
def home():
    return render_template('index.html')



@landingPage.route('/register', methods=['POST'])
def register():
    email = request.form.get("email")
    print(email)
    return (redirect(url_for('landingPage.home')))
