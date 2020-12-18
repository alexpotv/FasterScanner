from scanutils.scanutils import *
from saveutils.saveutils import *

SAVE_PATH = "saved_images/"

print("Listing devices:\n" + str(list_devices()))

print("Scanning using first device")

image = scan_image(list_devices()[0], 300)

print("Image scanned")

save_image(image, get_next_filename())

print("Image saved")
