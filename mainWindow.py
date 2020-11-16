# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import adminWindow
import preferenceWindow

class Ui_mainWindow(object):
    def openPrefWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = preferenceWindow.Ui_prefMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAdminWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = adminWindow.Ui_adminMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.WindowModal)
        mainWindow.resize(529, 256)
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonPrediction = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPrediction.setGeometry(QtCore.QRect(90, 110, 151, 51))

        self.buttonPrediction.setObjectName("buttonPrediction")
        self.buttonPrediction.clicked.connect(self.openPrefWindow)

        self.buttonAdmin = QtWidgets.QPushButton(self.centralwidget)

        self.buttonAdmin.setGeometry(QtCore.QRect(300, 110, 151, 51))
        self.buttonAdmin.setObjectName("buttonAdmin")
        self.buttonAdmin.clicked.connect(self.openAdminWindow)
        self.labGREAnalyzer = QtWidgets.QLabel(self.centralwidget)
        self.labGREAnalyzer.setGeometry(QtCore.QRect(90, 50, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.labGREAnalyzer.setFont(font)
        self.labGREAnalyzer.setAlignment(QtCore.Qt.AlignCenter)
        self.labGREAnalyzer.setObjectName("labGREAnalyzer")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.buttonPrediction.setText(_translate("mainWindow", "Prediction"))
        self.buttonAdmin.setText(_translate("mainWindow", "Admin"))
        self.labGREAnalyzer.setText(_translate("mainWindow", "GRE Analyzer"))


if __name__ == "__main__":
    import sys
    import cx_Oracle
    connection = cx_Oracle.connect("piyush/piyushchaudhari@localhost")
    cursor = connection.cursor()

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
