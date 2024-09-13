import requests
import smtplib
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
    <body style="font-family: Arial, sans-serif; color: #333; background-color: #f4f4f9;">
        <div style="max-width: 600px; margin: auto; padding: 30px; border: 1px solid #ddd; border-radius: 15px; background-color: white;">
            <h2 style="color: #1a73e8; text-align: center;">Welcome to <span style="font-weight: bold;">TechStore</span>!</h2>
            
            <p style="font-size: 1.1em; line-height: 1.6; text-align: center;">
                We're excited to have you join us! <strong>TechStore</strong> is a platform designed to bridge the gap between users and tech providers, creating a seamless way to discover the latest gadgets and connect with your favorite tech vendors.
            </p>
            
            <div style="text-align: center; margin: 30px 0;">
                <img src="https://tailwindflex.com/storage/thumbnails/simple-coming-soon-page-2/canvas.min.webp?v=1" alt="Coming Soon" style="max-width: 100%; border-radius: 10px;">
            </div>
            
            <p style="font-size: 1.1em; line-height: 1.6;">
                We’re getting ready to launch something incredible very soon! Our mission is to make it easy for you to connect with the best tech gadgets and the people behind them. Whether you're a tech enthusiast or a gadget geek, you'll find something exciting on <strong>TechStore</strong>.
            </p>
            
            <p style="font-size: 1.1em; line-height: 1.6; text-align: center;">
                Here’s what to expect:
            </p>
            
            <ul style="list-style-type: square; padding-left: 20px; font-size: 1.1em;">
                <li><strong>Exclusive Access:</strong> Be among the first to explore our tech gadgets as soon as we launch.</li>
                <li><strong>Stay Informed:</strong> We’ll keep you in the loop with all the latest updates and offers.</li>
                <li><strong>Connect:</strong> Easily reach out to tech providers and get personalized support.</li>
            </ul>
            <p style="margin-top: 40px; font-size: 1em; text-align: center;">Thank you for joining us on this exciting journey!</p>

            <p style="text-align: center; font-weight: bold; font-size: 1.2em;">The TechStore Team</p>

            <footer style="text-align: center; margin-top: 30px; color: #777;">
                <p>&copy; 2024 TechStore. All rights reserved.</p>
                <p><a href="https://example.com/unsubscribe" style="color: #1a73e8; text-decoration: none;">Unsubscribe</a> | <a href="https://example.com/privacy" style="color: #1a73e8; text-decoration: none;">Privacy Policy</a></p>
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
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
