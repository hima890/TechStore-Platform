#!/usr/bin/python3
""" OPT code verification """
from datetime import datetime, timedelta



def isOtpValid(otp_creation_time):
    """Function to check OTP expiration"""
    # Get current time
    current_time = datetime.utcnow()

    # Calculate the time difference between now and the OTP creation time
    time_difference = current_time - otp_creation_time

    # Check if time difference is less than 10 minutes (600 seconds)
    if time_difference <= timedelta(minutes=10):
        return True
    else:
        return False
