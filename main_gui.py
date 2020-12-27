import sys
from PyQt5 import QtWidgets
from ui.FasterScannerMainWindow import MainWindow

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.showMaximized()
window.show()
app.exec()
