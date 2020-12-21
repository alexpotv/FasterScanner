from utilities.scanutils import ScanSession
from utilities.saveutils import *
from utilities.metadatautils import *
from datetime import datetime

SAVE_PATH = "saved_images/"

METADATA_DICT = {
    "Datetime": datetime(2000, 5, 23, 12, 0, 0),
    "ImageDescription": "Insert description here",
    "Orientation": 1
}

# Initializing scan session
scan_sess = ScanSession()

print("Listing devices:\n" + str(scan_sess.get_available_devices()))

print("Scanning using first device")

scan_sess.select_device_index()

scan_sess.virtual_scan_image()

print("Image scanned")

img = scan_sess.get_image()

save_image(img, get_next_filename(), build_exif_bytes(METADATA_DICT))

print("Image saved")
