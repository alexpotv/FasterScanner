"""
Utility class for a scanning session
"""

import pyinsane2
from PIL.BmpImagePlugin import BmpImageFile
from PIL import Image
from utilities.utilitiesExceptions.scanExceptions import *


class ScanSession:
    """
    Represents a scanner session
    """

    def __init__(self):
        """
        Constructor for ScanSession object
        """
        self.available_devices = []
        self.selected_device = "none"
        self.scanner_resolution = 300
        self.image = None

        self.update_devices_list()
        self.select_device_index()

    def select_device_index(self, index: int = 0):
        """
        Assigns the first available device as the current device
        :param index:
        :return: None
        """
        self.update_devices_list()
        try:
            self.selected_device = self.available_devices[index]
        except IndexError:
            self.selected_device = "none"

    def get_device(self):
        """
        Gets the current device's name
        :return: str: the name of the device
        """
        self.update_devices_list()
        return self.selected_device

    def get_available_devices(self):
        """
        Return the available devices
        :return: List<str> of available devices
        """
        self.update_devices_list()
        return self.available_devices

    def set_resolution(self, resolution: int):
        """
        Sets the resolution of the device
        :param resolution: the resolution of the device
        :return: None
        """
        self.scanner_resolution = resolution

    def get_resolution(self):
        """
        Gets the current resolution setting
        :return: int: The current resolution
        """
        return self.scanner_resolution

    def scan_image(self):
        """
        Performs the scan using the current device
        :return: None
        """
        self.update_devices_list()

        if self.selected_device == "none":
            raise DeviceUnavailable()
        if self.scanner_resolution < 0 or self.scanner_resolution > 600:
            raise InvalidResolution()

        pyinsane2.init()
        device = pyinsane2.Scanner(name=self.selected_device)

        pyinsane2.set_scanner_opt(device, 'resolution', [self.scanner_resolution])
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

        self.image = image

    def get_image(self):
        """
        Gets the last image scanned
        :return:
        """
        if self.image:
            return self.image
        else:
            raise NoImageScanned()

    def update_devices_list(self):
        """
        Updates the list the devices currently available
        :return: None
        """

        pyinsane2.init()
        devices = [x.name for x in pyinsane2.get_devices()]
        pyinsane2.exit()

        self.available_devices = devices

        if self.selected_device not in self.available_devices:
            self.selected_device = "none"

    def virtual_scan_image(self):
        """
        Performs a virtual scan, retrieves a dummy image
        :return: None
        """

        self.image = Image.new('RGB', (100, 100), 255)
