from unittest import TestCase
from utilities.saveutils import *
from utilities.metadatautils import build_exif_bytes
from datetime import datetime
import os
from pathlib import Path
from PIL import Image


BASE_PATH = "temp_test/"


class TestGetNextFilename(TestCase):
    def test_get_next_filename_0(self):
        # Creating the test directory environment under BASE_PATH
        os.mkdir(BASE_PATH)

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00000.jpg", "Case: empty directory")

        # Creating dummy files to populate the directory
        # The directory contains the following files:
        # IMG_00000.jpg
        # RandomFile1.jpg
        # RandomFile2.txt
        Path(BASE_PATH + "IMG_00000.jpg").touch()
        Path(BASE_PATH + "RandomFile1.jpg").touch()
        Path(BASE_PATH + "RandomFile2.txt").touch()

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00001.jpg", "Case: one image file already present")

        # Adding a random-numbered image file to the test directory
        Path(BASE_PATH + "IMG_00122.jpg").touch()

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00123.jpg", "Case: directory with non-continuous file numbers")

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        os.remove(BASE_PATH + "IMG_00000.jpg")
        os.remove(BASE_PATH + "IMG_00122.jpg")
        os.remove(BASE_PATH + "RandomFile1.jpg")
        os.remove(BASE_PATH + "RandomFile2.txt")
        os.rmdir(BASE_PATH)


class TestSaveImage(TestCase):
    def setUp(self) -> None:
        os.mkdir(BASE_PATH)

    def test_save_image_0(self):
        image = Image.new('RGB', (1, 1), 0)
        save_image(image, get_next_filename(BASE_PATH), None)
        self.assertTrue(os.path.exists(BASE_PATH + "IMG_00000.jpg"))

    def test_save_image_1(self):
        METADATA_DICT = {
            "Datetime": datetime(2000, 5, 23, 12, 0, 0),
            "ImageDescription": "Insert description here",
            "Orientation": 1
        }
        image = Image.new('RGB', (1, 1), 0)
        metadata = build_exif_bytes(METADATA_DICT)
        save_image(image, get_next_filename(BASE_PATH), metadata)
        self.assertTrue(os.path.exists(BASE_PATH + "IMG_00000.jpg"))

    def tearDown(self) -> None:
        os.remove(BASE_PATH + "IMG_00000.jpg")
        os.rmdir(BASE_PATH)
