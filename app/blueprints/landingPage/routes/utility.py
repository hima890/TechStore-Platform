from models import Email

def checkForExcringEmail(email):
    email = Email.query.filter_by(email=email).first()
    print(email)
    if email:
        return (True)
    return (False)
    