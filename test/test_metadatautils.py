from unittest import TestCase
import os
from datetime import datetime
from PIL import Image
from metadatautils.metadatautils import build_exif_bytes
import piexif

# Defining constants for file paths and names
BASEPATH = "test_temp/"
FILENAME = "IMG_TEST.jpg"

# Defining constant dictionary of metadata
METADATA_DICT = {
    "Datetime": datetime(2000, 1, 1, 12, 0, 0),
    "ImageDescription": "Test description",
    "Orientation": 1
}

class Test(TestCase):

    def setUp(self) -> None:
        # Creating temporary working directory
        os.mkdir(BASEPATH)

    def test_build_exif_bytes_0(self):
        # Building dummy image and saving with metadata
        test_image = Image.new('RGB', (1, 1), 0)
        exif_bytes_string = build_exif_bytes(METADATA_DICT)
        test_image.save(BASEPATH + FILENAME, exif=exif_bytes_string)

        # Reading image metadata
        loaded_data = piexif.load(BASEPATH + FILENAME)
        zeroth = loaded_data['0th']
        exif = loaded_data['Exif']
        first = loaded_data['1st']

        self.assertTrue(zeroth[piexif.ImageIFD.ImageDescription] == b"Test description")
        self.assertTrue(zeroth[piexif.ImageIFD.Orientation] == 1)
        self.assertTrue(zeroth[piexif.ImageIFD.Software] == b"FasterScanner")
        self.assertTrue(zeroth[piexif.ImageIFD.DateTime] == b"2000:01:01 12:00:00")

        self.assertTrue(exif[piexif.ExifIFD.DateTimeOriginal] == b"2000:01:01 12:00:00")

    def tearDown(self) -> None:
        # Removing created file
        os.remove(BASEPATH + FILENAME)

        # Removing working directory
        os.rmdir(BASEPATH)
