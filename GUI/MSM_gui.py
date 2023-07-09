import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
from MSM_PYQT5 import Ui_MainWindow


class MSM_MainWindow(QMainWindow):
    def __init__(self):
        super(MSM_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.fileButton1.clicked.connect(self.browse_image_files)
        self.ui.fileButton2.clicked.connect(self.browse_instrument_files)
        self.instrument_file_name = None
        self.image_file_name = None

    def browse_image_files(self):
        # Open File Dialog
        self.image_file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")

        # Output filename to screen
        if self.image_file_name:
            self.ui.musicsheet_image.setPixmap(QtGui.QPixmap(self.image_file_name))
            if self.instrument_file_name:
                self.ui.convertButton.setEnabled(True)
        else:
            self.ui.convertButton.setEnabled(False)
            self.ui.musicsheet_image.setPixmap(QtGui.QPixmap())

    def browse_instrument_files(self):
        # Open File Dialog
        self.instrument_file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")

        if self.instrument_file_name:
            # fait un truc
            if self.image_file_name:
                self.ui.convertButton.setEnabled(True)
        else:
            self.ui.convertButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MSM_MainWindow()
    gui.show()
    app.exec()
