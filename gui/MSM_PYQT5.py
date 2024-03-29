# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MSM_PYQT5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.musicsheet_txt = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.musicsheet_txt.sizePolicy().hasHeightForWidth()
        )
        self.musicsheet_txt.setSizePolicy(sizePolicy)
        self.musicsheet_txt.setMinimumSize(QtCore.QSize(50, 25))
        self.musicsheet_txt.setObjectName("musicsheet_txt")
        self.verticalLayout.addWidget(self.musicsheet_txt)
        self.fileButton1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileButton1.sizePolicy().hasHeightForWidth())
        self.fileButton1.setSizePolicy(sizePolicy)
        self.fileButton1.setObjectName("fileButton1")
        self.verticalLayout.addWidget(self.fileButton1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout.addItem(spacerItem)
        self.instrument_txt = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.instrument_txt.sizePolicy().hasHeightForWidth()
        )
        self.instrument_txt.setSizePolicy(sizePolicy)
        self.instrument_txt.setMinimumSize(QtCore.QSize(80, 30))
        self.instrument_txt.setObjectName("instrument_txt")
        self.verticalLayout.addWidget(self.instrument_txt)
        self.fileButton2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileButton2.sizePolicy().hasHeightForWidth())
        self.fileButton2.setSizePolicy(sizePolicy)
        self.fileButton2.setObjectName("fileButton2")
        self.verticalLayout.addWidget(self.fileButton2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 3, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.convertBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convertBar.sizePolicy().hasHeightForWidth())
        self.convertBar.setSizePolicy(sizePolicy)
        self.convertBar.setMinimumSize(QtCore.QSize(150, 0))
        self.convertBar.setProperty("value", 24)
        self.convertBar.setObjectName("convertBar")
        self.horizontalLayout.addWidget(self.convertBar)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.convertButton.sizePolicy().hasHeightForWidth()
        )
        self.convertButton.setSizePolicy(sizePolicy)
        self.convertButton.setMinimumSize(QtCore.QSize(0, 0))
        self.convertButton.setObjectName("convertButton")
        self.horizontalLayout.addWidget(self.convertButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.baseImage = QtWidgets.QWidget()
        self.baseImage.setObjectName("baseImage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.baseImage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.musicsheet_image = QtWidgets.QLabel(self.baseImage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.musicsheet_image.sizePolicy().hasHeightForWidth()
        )
        self.musicsheet_image.setSizePolicy(sizePolicy)
        self.musicsheet_image.setMinimumSize(QtCore.QSize(200, 200))
        self.musicsheet_image.setText("")
        self.musicsheet_image.setScaledContents(True)
        self.musicsheet_image.setObjectName("musicsheet_image")
        self.gridLayout_3.addWidget(self.musicsheet_image, 1, 0, 1, 1)
        self.tabWidget.addTab(self.baseImage, "")
        self.finishedImage = QtWidgets.QWidget()
        self.finishedImage.setObjectName("finishedImage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.finishedImage)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget.addTab(self.finishedImage, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MSM Converter"))
        self.musicsheet_txt.setText(_translate("MainWindow", "Music Sheet"))
        self.fileButton1.setText(_translate("MainWindow", "Select File"))
        self.instrument_txt.setText(_translate("MainWindow", "MIDI Instrument"))
        self.fileButton2.setText(_translate("MainWindow", "Select File"))
        self.convertButton.setText(_translate("MainWindow", "Convert File"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.baseImage),
            _translate("MainWindow", "Base Image"),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.finishedImage),
            _translate("MainWindow", "Finished Image"),
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
