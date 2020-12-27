"""
FasterScannerMainWindow class for the main window of the app
"""
import sys
from PyQt5 import QtWidgets, uic

from .MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

