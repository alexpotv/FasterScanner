"""
Image metadata utilities
"""

import piexif


def build_exif_bytes(metadata: dict):
    """
    Builds the EXIF data in the form of bytes
    :param metadata: The metadata to convert to bytes
    :return: String: the string of EXIF data bytes
    """

    timestamp_format = "%Y:%m:%d %H:%M:%S"
    timestamp = metadata["Datetime"]

    zeroth_ifd = {
        piexif.ImageIFD.ImageDescription: metadata["ImageDescription"],
        piexif.ImageIFD.Orientation: metadata["Orientation"],
        piexif.ImageIFD.Software: u"FasterScanner",
        piexif.ImageIFD.DateTime: timestamp.strftime(timestamp_format)
    }
    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: timestamp.strftime(timestamp_format)
    }
    gps_ifd = {}
    first_ifd = {
        piexif.ImageIFD.ImageDescription: metadata["ImageDescription"],
        piexif.ImageIFD.Orientation: metadata["Orientation"],
        piexif.ImageIFD.Software: u"FasterScanner",
        piexif.ImageIFD.DateTime: timestamp.strftime(timestamp_format)
    }

    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd, "GPS": gps_ifd, "1st": first_ifd, "thumbnail": None}
    exif_bytes = piexif.dump(exif_dict)

    return exif_bytes
