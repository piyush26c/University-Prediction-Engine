# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'successMsg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_successMainWindow(object):
    def setupUi(self, successMainWindow):
        successMainWindow.setObjectName("successMainWindow")
        successMainWindow.resize(327, 105)
        successMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(successMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelSuccessMsg = QtWidgets.QLabel(self.centralwidget)
        self.labelSuccessMsg.setGeometry(QtCore.QRect(60, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSuccessMsg.setFont(font)
        self.labelSuccessMsg.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.labelSuccessMsg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSuccessMsg.setObjectName("labelSuccessMsg")

        successMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(successMainWindow)
        self.statusbar.setObjectName("statusbar")
        successMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(successMainWindow)
        QtCore.QMetaObject.connectSlotsByName(successMainWindow)

    def retranslateUi(self, successMainWindow):
        _translate = QtCore.QCoreApplication.translate
        successMainWindow.setWindowTitle(_translate("successMainWindow", "MainWindow"))
        self.labelSuccessMsg.setText(_translate("successMainWindow", "Analyze operation Successful"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    successMainWindow = QtWidgets.QMainWindow()
    ui = Ui_successMainWindow()
    ui.setupUi(successMainWindow)
    successMainWindow.show()
    sys.exit(app.exec_())
