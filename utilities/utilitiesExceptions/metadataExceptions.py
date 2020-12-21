"""
Exceptions for the EXIFWriter class
"""


class InvalidOrientation(Exception):
    def __init__(self, msg: str = "The provided orientation is invalid"):
        super(InvalidOrientation, self).__init__()
        self.message = msg

    def __str__(self):
        return self.message
