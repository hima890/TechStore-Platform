#!/usr/bin/python3
"""Utility function to save and resize a profile picture."""
import os
from PIL import Image
from werkzeug.utils import secure_filename


def saveProfilePicture(pictureFile, outputSize=(300, 300), uploadFolder='static/profile_pics'):
    """
    Resizes and saves the profile picture.

    Parameters:
    - pictureFile: The uploaded picture file.
    - outputSize: Tuple specifying the size to resize the image to (default is 300x300).
    - uploadFolder: The folder where the image will be saved (default is 'static/profile_pics').

    Returns:
    - filename: The name of the saved file.
    - picture_path: The full path to the saved file.
    """

    # Secure the filename
    filename = secure_filename(pictureFile.filename)
    
    # Ensure the upload folder exists
    if not os.path.exists(uploadFolder):
        os.makedirs(uploadFolder)
    
    # Set the path where the file will be saved
    picture_path = os.path.join(uploadFolder, filename)
    
    # Resize and save the image
    img = Image.open(pictureFile)
    img.thumbnail(outputSize)
    img.save(picture_path)
    
    return filename, picture_path
