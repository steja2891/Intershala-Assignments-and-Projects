# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Book_Shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
Book = sqlite3.connect("Book_Database.db")

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ledit1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.ledit1.setFont(font)
        self.ledit1.setObjectName("ledit1")
        self.horizontalLayout.addWidget(self.ledit1)
        self.b1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.BookChecking)
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ledit2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.ledit2.setFont(font)
        self.ledit2.setStyleSheet("QLineEdit#ledit2{\n"
        "color: rgb(0, 85, 255)\n"
        "}")
        self.ledit2.setFrame(False)
        self.ledit2.setObjectName("ledit2")
        self.horizontalLayout_2.addWidget(self.ledit2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ledit3 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.ledit3.setFont(font)
        self.ledit3.setObjectName("ledit3")
        self.ledit3.setValidator(QtGui.QIntValidator())
        self.horizontalLayout_3.addWidget(self.ledit3)
        self.b2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.BookQuantity)
        self.horizontalLayout_3.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ledit4 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.ledit4.setFont(font)
        self.ledit4.setStyleSheet("QLineEdit#ledit4{\n"
        "color: rgb(0, 85, 255)\n"
        "}")
        self.ledit4.setFrame(False)
        self.ledit4.setObjectName("ledit4")
        self.horizontalLayout_4.addWidget(self.ledit4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.b3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.verticalLayout.addWidget(self.b3)

        self.retranslateUi(Form)
        self.b3.clicked.connect(self.ledit1.clear)
        self.b3.clicked.connect(self.ledit2.clear)
        self.b3.clicked.connect(self.ledit3.clear)
        self.b3.clicked.connect(self.ledit4.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Book_Shop"))
        self.label.setText(_translate("Form", "Book Name: "))
        self.ledit1.setPlaceholderText(_translate("Form", "Enter the Book Title"))
        self.ledit3.setPlaceholderText(_translate("Form", "Enter the Quantity of Book"))
        self.b1.setText(_translate("Form", "Find Price"))
        self.label_2.setText(_translate("Form", "Price:              "))
        self.label_3.setText(_translate("Form", "Quantity:"))
        self.b2.setText(_translate("Form", "Find Total "))
        self.label_4.setText(_translate("Form", "Total:       "))
        self.b3.setText(_translate("Form", "Reset"))

    def BookChecking(self):
        Book_Name = self.ledit1.text()
        Data = "SELECT * from BookDetails WHERE Name='"+Book_Name+"';"
        b = Book.cursor()
        b.execute(Data)
        result = b.fetchall()
        if result == []:
            msg = QMessageBox()
            msg.setWindowTitle("Message")
            msg.setText("Sorry, The Book is Not Available right now!")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
            msg.setInformativeText("Please come back later..:)")
            x = msg.exec_()
        else:
            global re
            price_data = "SELECT price FROM BookDetails WHERE Name = '"+Book_Name+"';"
            price = b.execute(price_data)
            re = price.fetchall()
            self.ledit2.setText("Rs :"+str(re[0][0]))

    def BookQuantity(self):
        Quantity = self.ledit3.text()
        Q = int(Quantity)
        self.ledit4.setText("Rs: {}".format(Q*re[0][0]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())