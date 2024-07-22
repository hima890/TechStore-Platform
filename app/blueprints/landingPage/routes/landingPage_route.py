from flask import Blueprint, render_template, request, redirect, url_for
from blueprints import db
from models import Email

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
    formEmail = request.form.get("email")
    addnewEmail = Email(email=formEmail)
    db.session.add(addnewEmail)
    db.session.commit()
    return (redirect(url_for('landingPage.home')))
