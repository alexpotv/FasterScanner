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

        self.data_editor_setup()

    def data_editor_setup(self):
        # Date editor and checkbox
        self.saveDateMetadata.setChecked(True)
        self.saveDateMetadata.stateChanged.connect(lambda: self.dateField.setEnabled(self.saveDateMetadata.isChecked()))

        # Time editor and checkbox
        self.saveTimeMetadata.setChecked(True)
        self.saveTimeMetadata.stateChanged.connect(lambda: self.timeField.setEnabled(self.saveTimeMetadata.isChecked()))

        # Image description editor and checkbox
        self.saveImageDescriptionMetadata.setChecked(True)
        self.saveImageDescriptionMetadata.stateChanged.connect(lambda: self.imageDescriptionField.setEnabled(
            self.saveImageDescriptionMetadata.isChecked()
        ))

        # Orientation editor and checkbox
        self.saveOrientationMetadata.setChecked(True)
        self.saveOrientationMetadata.stateChanged.connect(lambda: self.orientationSwitchWidget.setEnabled(
            self.saveOrientationMetadata.isChecked()
        ))

    def toggle_date_field(self):
        if self.dateField.isEnabled():
            self.dateField.setDisabled(True)
        else:
            self.dateField.setDisabled(False)
