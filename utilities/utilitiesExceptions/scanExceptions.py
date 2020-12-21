"""
Exceptions for the ScanSession class
"""


class DeviceUnavailable(Exception):
    def __init__(self, msg: str = "The selected device is unavailable"):
        super(DeviceUnavailable, self).__init__()
        self.message = msg

    def __str__(self):
        return self.message

class InvalidResolution(Exception):
    def __init__(self, msg: str = "The resolution set for the scanner is invalid"):
        super(InvalidResolution, self).__init__()
        self.message = msg

    def __str__(self):
        return self.message

class NoImageScanned(Exception):
    def __init__(self, msg: str = "No scan has been performed. Cannot retrieve image"):
        super(NoImageScanned, self).__init__()
        self.message = msg

    def __str__(self):
        return self.message
