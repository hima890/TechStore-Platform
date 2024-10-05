#!/usr/bin/python3
"""Utility function to save and resize a profile picture."""
import os, uuid
from PIL import Image
from werkzeug.utils import secure_filename


def saveProfilePictureFunc(pictureFile, outputSize=(300, 300), uploadFolder='static/profile_pics'):
    """
    Rename using uuid4 and resizes and saves the profile picture.

    Parameters:
    - pictureFile: The uploaded picture file.
    - outputSize: Tuple specifying the size to resize the image to (default is 300x300).
    - uploadFolder: The folder where the image will be saved (default is 'static/profile_pics').

    Returns:
    - filename: The new name of the saved file.
    - picture_path: The full path to the saved file.
    """

    # Secure the filename by obtining a safe version of it
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
    
    return unique_filename, picture_path
