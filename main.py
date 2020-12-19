from scanutils.scanutils import *
from saveutils.saveutils import *
from metadatautils.metadatautils import *
from datetime import datetime

SAVE_PATH = "saved_images/"

METADATA_DICT = {
    "Datetime": datetime(2000, 5, 23, 12, 0, 0),
    "ImageDescription": "Insert description here",
    "Orientation": 1
}

print("Listing devices:\n" + str(list_devices()))

print("Scanning using first device")

image = scan_image(list_devices()[0], 300)

print("Image scanned")

save_image(image, get_next_filename(), build_exif_bytes(METADATA_DICT))

print("Image saved")
