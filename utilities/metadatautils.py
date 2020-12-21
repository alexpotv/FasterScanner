"""
Image metadata utilities
"""

import piexif
from datetime import datetime
from .utilitiesExceptions.metadataExceptions import *


class EXIFWriter:
    def __init__(self, p_datetime: datetime = None, p_description: str = None, p_orientation: int = None):
        if p_orientation < 1 or p_orientation > 8:
            raise InvalidOrientation()
        self.imageDescription = p_description
        self.datetime = p_datetime
        self.orientation = p_orientation
        self.software = "FasterScanner"

    def build_exif_bytes(self):
        timestamp_format = "%Y:%m:%d %H:%M:%S"

        zeroth_ifd = {}
        exif_ifd = {}
        gps_ifd = {}
        first_ifd = {}

        if self.imageDescription:
            zeroth_ifd[piexif.ImageIFD.ImageDescription] = self.imageDescription
        if self.datetime:
            zeroth_ifd[piexif.ImageIFD.DateTime] = self.datetime.strftime(timestamp_format)
            exif_ifd[piexif.ExifIFD.DateTimeOriginal] = self.datetime.strftime(timestamp_format)
        if self.software:
            zeroth_ifd[piexif.ImageIFD.Software] = self.software
        if self.orientation:
            zeroth_ifd[piexif.ImageIFD.Orientation] = self.orientation

        exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd, "thumbnail": None}
        return piexif.dump(exif_dict)

