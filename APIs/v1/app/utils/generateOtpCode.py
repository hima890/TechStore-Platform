#!/usr/bin/python3
""" Generate the OTP """
from datetime import datetime
import random


def generate_otp():
    """Function to generate OTP and return OPT code and and creation time"""
    otp = random.randint(100000, 999999)
    created_at = datetime.now()
    return otp, created_at
