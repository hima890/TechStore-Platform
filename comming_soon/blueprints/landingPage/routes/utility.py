import requests
from models import Email
from config import ProConfig
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def checkForExcringEmail(email):
    """"Check if the email already in the database"""
    email = Email.query.filter_by(email=email).first()
    if email:
        return True
    return False


def userRegistration(email):
    """Your logic for registering the user goes here"""
    sender_email = ProConfig.SENDER_EMAIL
    sender_password = ProConfig.SENDER_PASSWORD
    server = ProConfig.SMTP_SERVER
    serverPort = ProConfig.SMTP_PORT
    subject = "Welcome to TechStore!"

    # HTML email content
    html_content = """
    <html>
    <body style="font-family: Arial, sans-serif; color: #333;">
        <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
            <h2 style="color: #444;">Welcome to <span style="color: #1a73e8;">TechStore</span>!</h2>
            <p>Thank you for registering with us. We are thrilled to have you on board.</p>
            <p style="font-size: 1.1em;">Here are some next steps:</p>
            <ul style="list-style-type: square;">
                <li><strong>Explore:</strong> Browse our latest tech gadgets.</li>
                <li><strong>Stay Updated:</strong> Subscribe to our newsletter for updates.</li>
                <li><strong>Get Support:</strong> Contact us anytime for help.</li>
            </ul>
            <p style="margin-top: 30px;">Best Regards,<br><strong>The TechStore Team</strong></p>
            <footer style="text-align: center; margin-top: 20px; color: #777;">
                <p>&copy; 2024 TechStore. All rights reserved.</p>
            </footer>
        </div>
    </body>
    </html>
    """

    # Create the email
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email

    # Attach the HTML content to the email
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Connect to the email server and send the email
        server = smtplib.SMTP(server, serverPort)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
