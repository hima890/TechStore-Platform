#!/usr/bin/python3
"""Utility function to save and resize a product image."""
import os
import uuid
from PIL import Image
from werkzeug.utils import secure_filename

def updateProductImage(pictureFile, outputSize=(600, 600), uploadFolder='static/products_images'):
    """
    Rename using uuid4 and resize and save the product picture.

    Parameters:
    - pictureFile: The uploaded picture file.
    - outputSize: Tuple specifying the size to resize the image to (default is 600x600).
    - uploadFolder: The folder where the image will be saved (default is 'static/products_images').

    Returns:
    - filename: The new name of the saved file.
    - picture_path: The full path to the saved file.
    """

    # Secure the filename by obtaining a safe version of it
    secureFile = secure_filename(pictureFile.filename)
    
    # Extract the file extension
    _, file_extension = os.path.splitext(secureFile)

    # Generate a unique file name using uuid4
    unique_filename = str(uuid.uuid4()) + file_extension

    # Ensure the upload folder exists
    if not os.path.exists(uploadFolder):
        os.makedirs(uploadFolder)
    
    # Set the path where the file will be saved
    picture_path = os.path.join(uploadFolder, unique_filename)
    
    # Resize and save the image
    img = Image.open(pictureFile)
    img.thumbnail(outputSize)
    img.save(picture_path)

    # Return the new file name and the path to the saved image
    return unique_filename, picture_path
