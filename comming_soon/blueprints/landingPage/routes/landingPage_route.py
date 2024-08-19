from flask import Blueprint, render_template, request, redirect, url_for, flash
from blueprints import db
from models import Email
from .utility import checkForExcringEmail, userRegistration

landingPage = Blueprint('landingPage', __name__,
                        static_folder='../static',
                        template_folder='../templates',
                        static_url_path='/static/landingPage')


@landingPage.route('/')
@landingPage.route('/home')
def home():
    return render_template('index.html')



@landingPage.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        formEmail = request.form.get("email")
        if not formEmail:
            # Flash an error message
            flash('Please inter your Email.', 'error')
        else:
            if checkForExcringEmail(formEmail):
                # Flash an error message
                flash('Email already registrated.' , 'secondary')
            else:
                # Process the email registration
                addnewEmail = Email(email=formEmail)
                db.session.add(addnewEmail)
                db.session.commit()
                # Send the welcome email
                userRegistration(formEmail)
                flash('Your email has been registered successfully!', 'success')
                return (redirect(url_for('landingPage.home')))
            

    return (render_template('index.html'))
