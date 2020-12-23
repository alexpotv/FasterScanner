"""
FasterScannerMainWindow class for the main window of the app
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class FasterScannerMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        """
        Constructor for the FasterScannerMainWindow class
        """
        super(FasterScannerMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("FasterScanner")

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()

        self.init_data_editor()

        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

    def init_data_editor(self):
        """
        Initializing the data editor panel
        :return: None
        """

        # Data Editor column widget and associated layout
        self.data_editor_widget = QWidget()
        data_editor_layout = QVBoxLayout()

        # Adding widgets to layout
        data_editor_layout.addWidget(QLabel("Test"))

        self.data_editor_widget.setLayout(data_editor_layout)

        self.main_layout.addWidget(self.data_editor_widget)
