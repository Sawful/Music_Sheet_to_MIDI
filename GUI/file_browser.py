import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from MSM_gui import Ui_MainWindow

class MSM_MainWindow(QDialog):
    def __init__(self):
        super(MSM_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.browse_button.clicked.connect(self.browsefiles)


    def browse_files(self):
        print("coucou")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MSM_MainWindow()
    gui.show()
    app.exec()
