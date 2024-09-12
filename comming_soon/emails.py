import os
import smtplib
from flask import Flask, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv("../.env")

app = Flask(__name__)
# Set the sekrite key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SENDER_EMAIL'] = os.getenv('SENDER_EMAIL')
app.config['SENDER_PASSWORD'] = os.getenv('SENDER_PASSWORD')
app.config['SMTP_SERVER'] = os.getenv('SMTP_SERVER')
app.config['SMTP_PORT'] = os.getenv('SMTP_PORT')

@app.route('/send_welcome_email', methods=['POST'])
def send_welcome_email():
    data = request.get_json()
    recipient_email = data['email']
    send_email(recipient_email)
    return jsonify({"message": "Welcome email sent!"}), 200

def send_email(recipient):
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
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
    msg['To'] = recipient

    # Attach the HTML content to the email
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Connect to the email server and send the email
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app.run(port=5005, debug=True)
