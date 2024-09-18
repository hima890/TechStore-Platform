#!/usr/bin/python3
""" Generate the product id code """
import random


def generateProductId():
    """Generate a random 4-digit number for product_id."""
    return random.randint(1000, 9999)
