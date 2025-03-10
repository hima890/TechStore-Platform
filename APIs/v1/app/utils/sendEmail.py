#!/usr/bin/python3
""" Utility functions for sending emails """
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(recipient, htmlContent, plainTextContent, subject):
    """ Send an email to the recipient with the specified HTML and plain text content

    Args:
        recipient (str): The email address of the recipient
        htmlContent (str): The HTML content of the email
        plainTextContent (str): The plain text content of the email
        subject (str): The subject of the email
    """
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    # Create the email with both plain text and HTML parts
    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    # Attach the plain text and HTML content to the email
    msg.attach(MIMEText(plainTextContent, "plain"))
    msg.attach(MIMEText(htmlContent, "html"))

    try:
        # Connect to the email server and send the email
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
    except Exception as e:
        print("Failed to send email: {}".format(e))
        return False

    return True
