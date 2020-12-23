import sys
from PyQt5 import QtWidgets
from ui.FasterScannerMainWindow import FasterScannerMainWindow

app = QtWidgets.QApplication(sys.argv)

window = FasterScannerMainWindow()
window.showMaximized()
window.show()
app.exec()
