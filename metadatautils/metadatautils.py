"""
Image metadata utilities
"""

import piexif
from datetime import date


def build_exif_bytes(timestamp: date, x_resolution: int = 300, y_resolution: int = 300):
    """
    Builds the EXIF data in the form of bytes
    :param timestamp: The date of the picture
    :return: String: the string of EXIF data bytes
    """

    zeroth_ifd = {
        piexif.ImageIFD.XResolution: (x_resolution, 1),
        piexif.ImageIFD.YResolution: (y_resolution, 1),
        piexif.ImageIFD.Software: u"FasterScanner"
    }
    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: str(timestamp.year) + ":" + str(timestamp.month) + ":" + str(timestamp.day) + " 00:00:00"
    }

    exif_dict = {"Exif": exif_ifd}
    exif_bytes = piexif.dump(exif_dict)

    return exif_bytes
