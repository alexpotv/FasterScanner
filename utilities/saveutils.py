"""
Image file save utilities
"""

import os
import re
from PIL import BmpImagePlugin


def get_next_filename(base_path: str = "saved_images/"):
    """
    Generates the filename for the next image to be saved
    :param base_path: The base filepath to save the images to
    :return: String: The path of the next image file to be saved
    """

    # Listing files matching IMG_XXXXX.jpg pattern
    file_nums = [x.split('_')[-1] for x in os.listdir(base_path) if re.match(r"IMG_[0-9]{5}\.jpg", x)]

    # If no files matching the pattern are present
    if len(file_nums) == 0:
        return base_path + "IMG_00000.jpg"

    # Keeping only image file number
    file_nums = [x.split('.')[0] for x in file_nums]
    # Casting list elements to integer
    file_nums = [int(x) for x in file_nums]

    # Getting the next integer to use as a filename
    next_file_number_str = str(max(file_nums) + 1)
    while len(next_file_number_str) != 5:
        next_file_number_str = "0" + next_file_number_str

    return base_path + "IMG_" + next_file_number_str + ".jpg"


def save_image(image: BmpImagePlugin.BmpImageFile, file_path: str, exif_bytes = None):
    """
    Saves the image to the specified location on disk
    :param exif_bytes: The EXIF data bytes to write to the image
    :param image: the image to save
    :param file_path: the file path to save the image to
    :return: None
    """
    if exif_bytes:
        image.save(file_path, exif=exif_bytes)
    else:
        image.save(file_path)
