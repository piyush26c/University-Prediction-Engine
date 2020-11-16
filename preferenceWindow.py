# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferenceWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import statistics
import errorCondition1
import successMsg
import errorCondition3
import errorCondition2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import  logicDB



import cx_Oracle




class Ui_prefMainWindow(object):

    def openError1Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = errorCondition1.Ui_errorMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openError2Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = errorCondition2.Ui_errorMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openError3Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = errorCondition3.Ui_errorMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSuccessWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = successMsg.Ui_successMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()



    def setupUi(self, prefMainWindow):
        prefMainWindow.setObjectName("prefMainWindow")
        prefMainWindow.resize(482, 455)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        prefMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(prefMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        uniList = ['piyush', 'rohit', 'lol']
        self.comboPref1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboPref1.setGeometry(QtCore.QRect(20, 100, 411, 22))
        self.comboPref1.setObjectName("comboPref1")

        universityList = ["Massachusetts Institute of Technology (MIT)",
                          "Stanford University",
                          "Harvard University",
                          "California Institute of Technology (Caltech)",
                          "University of Chicago",
                          "Princeton University",
                          "Cornell University",
                          "University of Pennsylvania",
                          "Yale University",
                          "Columbia University",
                          "University of Michigan",
                          "Johns Hopkins University",
                          "Duke University",
                          "University of California, Berkeley (UCB)",
                          "Northwestern University",
                          "University of California, Los Angeles (UCLA)",
                          "New York University (NYU)",
                          "University of California, San Diego (UCSD)",
                          "Carnegie Mellon University",
                          "University of Wisconsin-Madison",
                          "Brown University",
                          "University of Texas at Austin",
                          "University of Washington",
                          "Georgia Institute of Technology",
                          "University of Illinois at Urbana-Champaign",
                          "Rice University",
                          "University of North Carolina, Chapel Hill",
                          "Pennsylvania State University",
                          "Boston University",
                          "Australian National University",
                          "University of Melbourne",
                          "University of Sydney",
                          "University of New South Wales (UNSW Sydney)",
                          "University of Queensland",
                          "Monash University",
                          "University of Western Australia",
                          "Tsinghua University",
                          "Peking University",
                          "Fudan University",
                          "Zhejiang University",
                          "Shanghai Jiao Tong University",
                          "University of Science and Technology of China",
                          "University of Oxford",
                          "University of Cambridge",
                          "UCL (University College London)",
                          "Imperial College London",
                          "University of Edinburgh",
                          "University of Manchester",
                          "King's College London",
                          "London School of Economics and Political Science (LSE)",
                          "University of Bristol",
                          "University of Warwick",
                          "University of Glasgow",
                          "Durham University",
                          "University of Sheffield",
                          "University of Birmingham",
                          "University of Leeds",
                          "University of Nottingham",
                          "University of Southampton",
                          "University of St Andrews"]

        self.comboPref1.addItems(universityList)



        self.comboPref2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboPref2.setGeometry(QtCore.QRect(20, 170, 411, 22))
        self.comboPref2.setObjectName("comboPref2")
        self.comboPref2.addItems( universityList)

        self.comboPref3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboPref3.setGeometry(QtCore.QRect(20, 240, 411, 22))
        self.comboPref3.setObjectName("comboPref3")
        self.comboPref3.addItems(universityList)

        self.labelEnterPref = QtWidgets.QLabel(self.centralwidget)
        self.labelEnterPref.setGeometry(QtCore.QRect(110, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.labelEnterPref.setFont(font)
        self.labelEnterPref.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEnterPref.setObjectName("labelEnterPref")
        self.labelPref1 = QtWidgets.QLabel(self.centralwidget)
        self.labelPref1.setGeometry(QtCore.QRect(20, 65, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelPref1.setFont(font)
        self.labelPref1.setObjectName("labelPref1")
        self.labelPref2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPref2.setGeometry(QtCore.QRect(20, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelPref2.setFont(font)
        self.labelPref2.setObjectName("labelPref2")
        self.labelPref3 = QtWidgets.QLabel(self.centralwidget)
        self.labelPref3.setGeometry(QtCore.QRect(20, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelPref3.setFont(font)
        self.labelPref3.setObjectName("labelPref3")
        self.labelGREScore = QtWidgets.QLabel(self.centralwidget)
        self.labelGREScore.setGeometry(QtCore.QRect(110, 260, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.labelGREScore.setFont(font)
        self.labelGREScore.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGREScore.setObjectName("labelGREScore")
        self.textGREScore = QtWidgets.QTextEdit(self.centralwidget)
        self.textGREScore.setGeometry(QtCore.QRect(170, 300, 104, 31))
        self.textGREScore.setObjectName("textGREScore")

        self.buttonAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAnalyze.setGeometry(QtCore.QRect(160, 340, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonAnalyze.setFont(font)
        self.buttonAnalyze.setObjectName("buttonAnalyze")
        self.buttonAnalyze.clicked.connect(self.pressed)

        prefMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(prefMainWindow)
        self.statusbar.setObjectName("statusbar")
        prefMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(prefMainWindow)
        QtCore.QMetaObject.connectSlotsByName(prefMainWindow)







    def pressed(self):
        print(self.comboPref1.currentText())
        print(self.comboPref2.currentText())
        print(self.comboPref3.currentText())
        pref1 = self.comboPref1.currentText()
        pref2 = self.comboPref2.currentText()
        pref3 = self.comboPref3.currentText()

        # GRE score entered by the user in preferences window
        entGREScore = int(self.textGREScore.toPlainText().strip())
        print(entGREScore)

        prefFlag = False
        GREScoreFlag = False
        if pref1 == pref2 or pref1 == pref3 or pref2 == pref3:
                prefFlag = True
        if entGREScore > 340 or entGREScore <= 0:
                GREScoreFlag = True
        if prefFlag == True and GREScoreFlag == False:
            self.openError1Window()
        elif prefFlag == False and GREScoreFlag == True:
            self.openError2Window()
            self.textGREScore.clear()
        elif prefFlag == True and GREScoreFlag == True:
            self.openError3Window()
            self.textGREScore.clear()
        else:
            self.openSuccessWindow()
            logicDB.logicDBFunc(pref1, pref2, pref3)










    def retranslateUi(self, prefMainWindow):
        _translate = QtCore.QCoreApplication.translate
        prefMainWindow.setWindowTitle(_translate("prefMainWindow", "MainWindow"))
        self.labelEnterPref.setText(_translate("prefMainWindow", "Enter your preferences"))
        self.labelPref1.setText(_translate("prefMainWindow", "Preference-1"))
        self.labelPref2.setText(_translate("prefMainWindow", "Preference-2"))
        self.labelPref3.setText(_translate("prefMainWindow", "Preference-3"))
        self.labelGREScore.setText(_translate("prefMainWindow", "Enter your GRE Score"))
        self.buttonAnalyze.setText(_translate("prefMainWindow", "Analyze"))


if __name__ == "__main__":

    import sys

    connection = cx_Oracle.connect("piyush/piyushchaudhari@localhost")

    app = QtWidgets.QApplication(sys.argv)
    prefMainWindow = QtWidgets.QMainWindow()
    ui = Ui_prefMainWindow()
    ui.setupUi(prefMainWindow)
    prefMainWindow.show()
    sys.exit(app.exec_())
