#!/usr/bin/python3
import os
from werkzeug.utils import secure_filename

def saveStoreImage(image, image_type):
    """
    Save an image file to a directory and return the filename and path.
    
    :param image: The image file from the request
    :param image_type: A string indicating the type of image ('inner' or 'outer')
    :return: A tuple of the filename and file path
    """
    # Define the upload directory (you might want to configure this in your settings)
    upload_dir = os.path.join(os.path.dirname(__file__), 'static', 'store_images')

    # Ensure the directory exists
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Secure the filename
    filename = secure_filename(image.filename)
    file_path = os.path.join(upload_dir, filename)

    # Save the file
    image.save(file_path)

    return filename, file_path
