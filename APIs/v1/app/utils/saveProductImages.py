#!/usr/bin/python3
"""Utility function to save and resize a profile picture."""
import os, uuid
from PIL import Image
from werkzeug.utils import secure_filename


def saveProductImagesFunc(pictureFiles, outputSize=(600, 600), uploadFolder='static/products_images'):
    """
    Rename using uuid4 and resizes and saves the products pictures.

    Parameters:
    - pictureFiles: List of uploaded picture files.
    - outputSize: Tuple specifying the size to resize the image to (default is 600x600).
    - uploadFolder: The folder where the images will be saved (default is 'static/products_images').

    Returns:
    - newFileNames: List of the new filenames of the saved files.
    - newFilePath: List of the full paths to the saved files.
    """

    # Place holder for pictures
    newFileNames = []
    newFilePath = []

    # Loop through the picture files
    for picture in pictureFiles:
        if picture:  # Ensure that the picture is not None
            # Secure the filename
            secureFile = secure_filename(picture.filename)
            
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
            img = Image.open(picture)
            img.thumbnail(outputSize)
            img.save(picture_path)

            # Add to the lists
            newFileNames.append(unique_filename)
            newFilePath.append(picture_path)
    
    # Return the list of file names and paths
    return newFileNames, newFilePath
