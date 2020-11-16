# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errorMsg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import  sys

class Ui_errorMainWindow(object):



    def setupUi(self, errorMainWindow):
        errorMainWindow.setObjectName("errorMainWindow")
        errorMainWindow.resize(327, 105)
        errorMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(errorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelErrorMsg = QtWidgets.QLabel(self.centralwidget)
        self.labelErrorMsg.setGeometry(QtCore.QRect(0, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelErrorMsg.setFont(font)
        self.labelErrorMsg.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.labelErrorMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelErrorMsg.setObjectName("labelErrorMsg")

        errorMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(errorMainWindow)
        self.statusbar.setObjectName("statusbar")
        errorMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(errorMainWindow)
        QtCore.QMetaObject.connectSlotsByName(errorMainWindow)

    def retranslateUi(self, errorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        errorMainWindow.setWindowTitle(_translate("errorMainWindow", "MainWindow"))
        self.labelErrorMsg.setText(_translate("errorMainWindow", "Error Occured : Enter the valid GRE Score (i.e <= 340)"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorMainWindow = QtWidgets.QMainWindow()
    ui = Ui_errorMainWindow()
    ui.setupUi(errorMainWindow)
    errorMainWindow.show()
    sys.exit(app.exec_())
