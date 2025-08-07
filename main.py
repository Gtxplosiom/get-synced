from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GetSynced")

        # can either drag the item over here
        # might need to pass a draggable class here and fetch the file location
        # or click and open file viewer and fetch the location
        # once fetched, store the location on a db using sqlite
        button = QPushButton("Drag a file here to sync")

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
