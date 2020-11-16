# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
connection = cx_Oracle.connect("piyush/piyushchaudhari@localhost")
# cursor = connection.cursor()


class Ui_adminMainWindow(object):

    def doUniInsert(self):
        cursor = connection.cursor()

        insertUniName = str(self.textUniInsertName.toPlainText().strip())
        insertUniWRank = int(self.textUniInsertWRank.toPlainText().strip())
        insertUniCountry = str(self.textUniInsertCountry.toPlainText().strip())
        queryInsert = f'INSERT INTO university_list VALUES (\'{insertUniName}\', {insertUniWRank}, \'{insertUniCountry}\')'
        queryInsert = queryInsert.strip()
        print(queryInsert)
        print(insertUniName)
        cursor.execute(queryInsert)
        connection.commit()
        # print("piyu")


    def doUniUpdate(self):
        cursor = connection.cursor()
        updateUniName = str(self.comboUniUpdateSelect.currentText().strip())
        updatedWorldRank = int(self.plainTextUniUpdateWRank.toPlainText().strip())

        qryToUpdateWR = f'UPDATE UNIVERSITY_LIST SET WORLD_RANK = {updatedWorldRank} WHERE UNIVERSITY_NAME = \'{updateUniName}\''
        print(qryToUpdateWR)
        qryToUpdateWR = qryToUpdateWR.strip()
        cursor.execute(qryToUpdateWR)
        connection.commit()


    def doUniDelete(self):
        cursor = connection.cursor()
        deleteUniName = str(self.comboUniDeleteSelect.currentText().strip())
        qryToDeleteUni = f'DELETE FROM UNIVERSITY_LIST WHERE UNIVERSITY_NAME = \'{deleteUniName}\''
        print(qryToDeleteUni)
        qryToDeleteUni = qryToDeleteUni.strip()
        cursor.execute(qryToDeleteUni)
        connection.commit()


    def doStuInsert(self):
        cursor = connection.cursor()
        insertedStudentname = str(self.textStudInsertName.toPlainText().strip())
        insertedStudUniversityname = str(self.textStudInsertUniName.toPlainText().strip())
        insertedStudGREScore = int(self.textStudInsertGREScore.toPlainText().strip())
        insertedStudTOEFLScore = int(self.textStudInsertTOEFLScore.toPlainText().strip())

        qryToInsertInAdmittedStud = f'INSERT INTO ADMITTED_STUDENTS VALUES (\'{insertedStudentname}\',\'{insertedStudUniversityname}\', {insertedStudGREScore}, {insertedStudTOEFLScore})'
        print(qryToInsertInAdmittedStud)
        qryToInsertInAdmittedStud = qryToInsertInAdmittedStud.strip()
        cursor.execute(qryToInsertInAdmittedStud)
        connection.commit()




    def setupUi(self, adminMainWindow):
        adminMainWindow.setObjectName("adminMainWindow")
        adminMainWindow.resize(744, 640)
        self.centralwidget = QtWidgets.QWidget(adminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelAdminPanel = QtWidgets.QLabel(self.centralwidget)
        self.labelAdminPanel.setGeometry(QtCore.QRect(280, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelAdminPanel.setFont(font)
        self.labelAdminPanel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAdminPanel.setObjectName("labelAdminPanel")
        self.labelMUniversities = QtWidgets.QLabel(self.centralwidget)
        self.labelMUniversities.setGeometry(QtCore.QRect(20, 46, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMUniversities.setFont(font)
        self.labelMUniversities.setObjectName("labelMUniversities")
        self.labelUniInsert = QtWidgets.QLabel(self.centralwidget)
        self.labelUniInsert.setGeometry(QtCore.QRect(20, 90, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelUniInsert.setFont(font)
        self.labelUniInsert.setObjectName("labelUniInsert")
        self.labelUniUpdate = QtWidgets.QLabel(self.centralwidget)
        self.labelUniUpdate.setGeometry(QtCore.QRect(20, 210, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelUniUpdate.setFont(font)
        self.labelUniUpdate.setObjectName("labelUniUpdate")
        self.comboUniUpdateSelect = QtWidgets.QComboBox(self.centralwidget)
        self.comboUniUpdateSelect.setGeometry(QtCore.QRect(60, 260, 291, 31))
        self.comboUniUpdateSelect.setObjectName("comboUniUpdateSelect")

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
        self.comboUniUpdateSelect.addItems(universityList)

        self.labelUniUpdateSelect = QtWidgets.QLabel(self.centralwidget)
        self.labelUniUpdateSelect.setGeometry(QtCore.QRect(150, 230, 101, 20))
        self.labelUniUpdateSelect.setObjectName("labelUniUpdateSelect")
        self.labelUniUpdateWRank = QtWidgets.QLabel(self.centralwidget)
        self.labelUniUpdateWRank.setGeometry(QtCore.QRect(460, 230, 31, 20))
        self.labelUniUpdateWRank.setObjectName("labelUniUpdateWRank")
        self.plainTextUniUpdateWRank = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextUniUpdateWRank.setGeometry(QtCore.QRect(430, 260, 91, 31))
        self.plainTextUniUpdateWRank.setObjectName("plainTextUniUpdateWRank")
        self.textUniInsertName = QtWidgets.QTextEdit(self.centralwidget)
        self.textUniInsertName.setGeometry(QtCore.QRect(60, 150, 251, 31))
        self.textUniInsertName.setObjectName("textUniInsertName")
        self.textUniInsertWRank = QtWidgets.QTextEdit(self.centralwidget)
        self.textUniInsertWRank.setGeometry(QtCore.QRect(320, 150, 91, 31))
        self.textUniInsertWRank.setObjectName("textUniInsertWRank")
        self.textUniInsertCountry = QtWidgets.QTextEdit(self.centralwidget)
        self.textUniInsertCountry.setGeometry(QtCore.QRect(430, 150, 141, 31))
        self.textUniInsertCountry.setObjectName("textUniInsertCountry")
        self.labelUniInsertName = QtWidgets.QLabel(self.centralwidget)
        self.labelUniInsertName.setGeometry(QtCore.QRect(140, 120, 101, 20))
        self.labelUniInsertName.setObjectName("labelUniInsertName")
        self.labelUniInsertWRank = QtWidgets.QLabel(self.centralwidget)
        self.labelUniInsertWRank.setGeometry(QtCore.QRect(330, 120, 71, 21))
        self.labelUniInsertWRank.setObjectName("labelUniInsertWRank")
        self.labelUniInsertCountry = QtWidgets.QLabel(self.centralwidget)
        self.labelUniInsertCountry.setGeometry(QtCore.QRect(470, 120, 51, 21))
        self.labelUniInsertCountry.setObjectName("labelUniInsertCountry")
        self.labelMStudent = QtWidgets.QLabel(self.centralwidget)
        self.labelMStudent.setGeometry(QtCore.QRect(20, 430, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelMStudent.setFont(font)
        self.labelMStudent.setObjectName("labelMStudent")
        self.labelStudInsert = QtWidgets.QLabel(self.centralwidget)
        self.labelStudInsert.setGeometry(QtCore.QRect(20, 460, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelStudInsert.setFont(font)
        self.labelStudInsert.setObjectName("labelStudInsert")
        self.labelStudInsertUniName = QtWidgets.QLabel(self.centralwidget)
        self.labelStudInsertUniName.setGeometry(QtCore.QRect(340, 490, 101, 20))
        self.labelStudInsertUniName.setObjectName("labelStudInsertUniName")
        self.labelStudInsertGREScore = QtWidgets.QLabel(self.centralwidget)
        self.labelStudInsertGREScore.setGeometry(QtCore.QRect(530, 490, 61, 21))
        self.labelStudInsertGREScore.setObjectName("labelStudInsertGREScore")
        self.labelStudInsertTOEFLScore = QtWidgets.QLabel(self.centralwidget)
        self.labelStudInsertTOEFLScore.setGeometry(QtCore.QRect(640, 490, 31, 21))
        self.labelStudInsertTOEFLScore.setObjectName("labelStudInsertTOEFLScore")
        self.textStudInsertUniName = QtWidgets.QTextEdit(self.centralwidget)
        self.textStudInsertUniName.setGeometry(QtCore.QRect(290, 530, 201, 31))
        self.textStudInsertUniName.setObjectName("textStudInsertUniName")
        self.textStudInsertGREScore = QtWidgets.QTextEdit(self.centralwidget)
        self.textStudInsertGREScore.setGeometry(QtCore.QRect(510, 530, 91, 31))
        self.textStudInsertGREScore.setObjectName("textStudInsertGREScore")
        self.textStudInsertTOEFLScore = QtWidgets.QTextEdit(self.centralwidget)
        self.textStudInsertTOEFLScore.setGeometry(QtCore.QRect(620, 530, 71, 31))
        self.textStudInsertTOEFLScore.setObjectName("textStudInsertTOEFLScore")
        self.textStudInsertName = QtWidgets.QTextEdit(self.centralwidget)
        self.textStudInsertName.setGeometry(QtCore.QRect(70, 530, 201, 31))
        self.textStudInsertName.setObjectName("textStudInsertName")
        self.labelStudInsertName = QtWidgets.QLabel(self.centralwidget)
        self.labelStudInsertName.setGeometry(QtCore.QRect(150, 490, 31, 20))
        self.labelStudInsertName.setObjectName("labelStudInsertName")
        self.labelUniDelete = QtWidgets.QLabel(self.centralwidget)
        self.labelUniDelete.setGeometry(QtCore.QRect(20, 320, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelUniDelete.setFont(font)
        self.labelUniDelete.setObjectName("labelUniDelete")
        self.comboUniDeleteSelect = QtWidgets.QComboBox(self.centralwidget)
        self.comboUniDeleteSelect.setGeometry(QtCore.QRect(60, 370, 291, 31))
        self.comboUniDeleteSelect.setObjectName("comboUniDeleteSelect")

        universityList1 = ["Massachusetts Institute of Technology (MIT)",
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

        self.comboUniDeleteSelect.addItems(universityList1)
        self.labelUniDeleteSelect = QtWidgets.QLabel(self.centralwidget)
        self.labelUniDeleteSelect.setGeometry(QtCore.QRect(150, 340, 101, 20))
        self.labelUniDeleteSelect.setObjectName("labelUniDeleteSelect")
        self.buttonUniInsert = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUniInsert.setGeometry(QtCore.QRect(620, 150, 81, 31))
        self.buttonUniInsert.setObjectName("buttonUniInsert")

        self.buttonUniInsert.clicked.connect(self.doUniInsert)

        self.buttonUniUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUniUpdate.setGeometry(QtCore.QRect(620, 260, 81, 31))
        self.buttonUniUpdate.setObjectName("buttonUniUpdate")
        self.buttonUniUpdate.clicked.connect(self.doUniUpdate)
        self.buttonUniDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUniDelete.setGeometry(QtCore.QRect(620, 370, 81, 31))
        self.buttonUniDelete.setObjectName("buttonUniDelete")

        self.buttonUniDelete.clicked.connect(self.doUniDelete)

        self.buttonStudentInsert = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStudentInsert.setGeometry(QtCore.QRect(320, 580, 81, 31))
        self.buttonStudentInsert.setObjectName("buttonStudentInsert")

        self.buttonStudentInsert.clicked.connect(self.doStuInsert)
        adminMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminMainWindow)
        self.statusbar.setObjectName("statusbar")
        adminMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(adminMainWindow)
        QtCore.QMetaObject.connectSlotsByName(adminMainWindow)

    def retranslateUi(self, adminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        adminMainWindow.setWindowTitle(_translate("adminMainWindow", "MainWindow"))
        self.labelAdminPanel.setText(_translate("adminMainWindow", "ADMIN PANEL"))
        self.labelMUniversities.setText(_translate("adminMainWindow", "UNIVERSITIES"))
        self.labelUniInsert.setText(_translate("adminMainWindow", "INSERT"))
        self.labelUniUpdate.setText(_translate("adminMainWindow", "UPDATE"))
        self.labelUniUpdateSelect.setText(_translate("adminMainWindow", "SELECT UNIVERSITY"))
        self.labelUniUpdateWRank.setText(_translate("adminMainWindow", "RANK"))
        self.labelUniInsertName.setText(_translate("adminMainWindow", " UNIVERSITY NAME"))
        self.labelUniInsertWRank.setText(_translate("adminMainWindow", "WORLD RANK"))
        self.labelUniInsertCountry.setText(_translate("adminMainWindow", "COUNTRY"))
        self.labelMStudent.setText(_translate("adminMainWindow", "STUDENTS GOT ADMITTED"))
        self.labelStudInsert.setText(_translate("adminMainWindow", "INSERT"))
        self.labelStudInsertUniName.setText(_translate("adminMainWindow", " UNIVERSITY NAME"))
        self.labelStudInsertGREScore.setText(_translate("adminMainWindow", "GRE SCORE"))
        self.labelStudInsertTOEFLScore.setText(_translate("adminMainWindow", "TOFEL"))
        self.labelStudInsertName.setText(_translate("adminMainWindow", "NAME"))
        self.labelUniDelete.setText(_translate("adminMainWindow", "DELETE"))
        self.labelUniDeleteSelect.setText(_translate("adminMainWindow", "SELECT UNIVERSITY"))
        self.buttonUniInsert.setText(_translate("adminMainWindow", "INSERT"))
        self.buttonUniUpdate.setText(_translate("adminMainWindow", "UPDATE"))
        self.buttonUniDelete.setText(_translate("adminMainWindow", "DELETE"))
        self.buttonStudentInsert.setText(_translate("adminMainWindow", "INSERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminMainWindow = QtWidgets.QMainWindow()
    ui = Ui_adminMainWindow()
    ui.setupUi(adminMainWindow)
    adminMainWindow.show()
    sys.exit(app.exec_())
