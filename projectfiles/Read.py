# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Read.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FORM(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(444, 577)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.fileedt = QtWidgets.QLineEdit(Form)
        self.fileedt.setMaximumSize(QtCore.QSize(300, 20))
        self.fileedt.setObjectName("fileedt")
        self.gridLayout.addWidget(self.fileedt, 3, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(108, 19))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 2)
        self.titleedt = QtWidgets.QLineEdit(Form)
        self.titleedt.setMaximumSize(QtCore.QSize(300, 20))
        self.titleedt.setObjectName("titleedt")
        self.gridLayout.addWidget(self.titleedt, 2, 1, 1, 2)
        self.openfbtn = QtWidgets.QPushButton(Form)
        self.openfbtn.setMaximumSize(QtCore.QSize(130, 23))
        self.openfbtn.setObjectName("openfbtn")
        self.gridLayout.addWidget(self.openfbtn, 3, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 5, 0, 1, 3)
        self.readbtn = QtWidgets.QPushButton(Form)
        self.readbtn.setMaximumSize(QtCore.QSize(130, 23))
        self.readbtn.setObjectName("readbtn")
        self.gridLayout.addWidget(self.readbtn, 4, 2, 1, 1)
        self.wronglbl = QtWidgets.QLabel(Form)
        self.wronglbl.setText("")
        self.wronglbl.setObjectName("wronglbl")
        self.gridLayout.addWidget(self.wronglbl, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(130, 16))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.themebtn = QtWidgets.QPushButton(Form)
        self.themebtn.setText("themebtn")
        self.themebtn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.themebtn, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Read"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Информация</span></p></body></html>"))
        self.openfbtn.setText(_translate("Form", "выбрать файл"))
        self.readbtn.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Чиать</span></p></body></html>"))
        self.readbtn.setText(_translate("Form", "Читать"))
        self.themebtn.setText(_translate("Form", "Тёмная"))
        self.label.setText(_translate("Form", "Название книги"))