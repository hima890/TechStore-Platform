#!/usr/bin/python3
""" Delete the product images from the server """
import os


def deleteProductImage(image):
    if image:
        # Get the image path in the server
        imagePath = os.path.join('static/products_images', image)
        # Try to delete the image
        try:
            if os.path.exists(imagePath):
                os.remove(imagePath)
                return True
        except Exception as e:
            return False         
