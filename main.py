from scanutils.scanutils import *

print("Listing devices:\n" + str(list_devices()))

print("Scanning using first device")

image = scan_image(list_devices()[0], 300)

image.show()
