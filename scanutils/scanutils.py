"""
Utilities for using the scanner
"""

import pyinsane2


def list_devices():
    """
    Lists the devices currently available
    :return: List<String>: The list of the available devices' names
    """

    pyinsane2.init()
    devices = [x.name for x in pyinsane2.get_devices()]
    pyinsane2.exit()

    return devices


def scan_image(scanner_name: str, resolution: int = 300):
    """
    Starts a scan using the Scanner object's name attribute
    :param scanner_name: the name attribute of the scanner object to use
    :return: Image
    """

    pyinsane2.init()
    device = pyinsane2.Scanner(name=scanner_name)

    pyinsane2.set_scanner_opt(device, 'resolution', [resolution])
    pyinsane2.set_scanner_opt(device, 'mode', ['color'])

    pyinsane2.maximize_scan_area(device)

    scan_session = device.scan(multiple=False)
    try:
        while True:
            scan_session.scan.read()
    except EOFError:
        pass
    image = scan_session.images[-1]

    pyinsane2.exit()

    return image