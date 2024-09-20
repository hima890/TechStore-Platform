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
            else:
                # Log or print if the file does not exist
                print(f"File not found: {imagePath}")
                return False
        except Exception as e:
            # Log or print the error for debugging purposes
            print(f"Error deleting image {image}: {e}")
            return False
    # Return False if no image was provided
    return False
