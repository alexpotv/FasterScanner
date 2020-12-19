from unittest import TestCase
from saveutils.saveutils import *
import os
from pathlib import Path


BASE_PATH = "temp_test/"


class Test(TestCase):
    def test_get_next_filename(self):
        # Creating the test directory environment under BASE_PATH
        try:
            os.mkdir(BASE_PATH)
        except OSError:
            self.fail("An exception was raised while creating the test environment.")

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00000.jpg", "Case: empty directory")

        # Creating dummy files to populate the directory
        # The directory contains the following files:
        # IMG_00000.jpg
        # RandomFile1.jpg
        # RandomFile2.txt
        Path(BASE_PATH + "IMG_00000.jpg").touch()
        Path(BASE_PATH + "RandomFile1.jpg").touch()
        Path(BASE_PATH + "RandomFile2.txt").touch()
        if not os.path.exists(BASE_PATH + "IMG_00000.jpg") and os.path.exists(
                BASE_PATH + "RandomFile1.jpg") and os.path.exists(BASE_PATH + "RandomFile2.txt"):
            self.fail("An exception was raised while creating the test environment.")

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00001.jpg", "Case: one image file already present")

        # Adding a random-numbered image file to the test directory
        Path(BASE_PATH + "IMG_00122.jpg").touch()
        if not os.path.exists(BASE_PATH + "IMG_00122.jpg"):
            self.fail("An exception was raised while creating the test environment.")

        self.assertEqual(get_next_filename(BASE_PATH), BASE_PATH + "IMG_00123.jpg", "Case: directory with non-continuous file numbers")

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        os.remove(BASE_PATH + "IMG_00000.jpg")
        os.remove(BASE_PATH + "IMG_00122.jpg")
        os.remove(BASE_PATH + "RandomFile1.jpg")
        os.remove(BASE_PATH + "RandomFile2.txt")
        os.rmdir(BASE_PATH)
