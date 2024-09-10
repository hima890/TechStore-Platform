import requests
from models import Email

def checkForExcringEmail(email):
    email = Email.query.filter_by(email=email).first()
    print(email)
    if email:
        return (True)
    return (False)

def userRegistration(email):
    # Your logic for registering the user goes here

    # Now, trigger the email microservice
    try:
        response = requests.post(
            'http://localhost:5005/send_welcome_email',
            json={'email': email}
        )
        if response.status_code == 200:
            print("Welcome email successfully sent.")
        else:
            print("Failed to send welcome email.")
    except Exception as e:
        print(f"Error contacting the email microservice: {e}")