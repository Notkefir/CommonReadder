# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Append_readlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UI_FORm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(345, 228)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.booknameedit = QtWidgets.QLineEdit(Form)
        self.booknameedit.setObjectName("booknameedit")
        self.gridLayout.addWidget(self.booknameedit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.authoredit = QtWidgets.QLineEdit(Form)
        self.authoredit.setObjectName("authoredit")
        self.gridLayout.addWidget(self.authoredit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.genreedit = QtWidgets.QLineEdit(Form)
        self.genreedit.setObjectName("genreedit")
        self.verticalLayout.addWidget(self.genreedit)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.selectfile = QtWidgets.QPushButton(Form)
        self.selectfile.setObjectName("selectfile")
        self.gridLayout.addWidget(self.selectfile, 4, 0, 1, 1)
        self.filenameedit = QtWidgets.QLineEdit(Form)
        self.filenameedit.setObjectName("filenameedit")
        self.gridLayout.addWidget(self.filenameedit, 4, 1, 1, 1)
        self.infwrong = QtWidgets.QLabel(Form)
        self.infwrong.setText("")
        self.infwrong.setObjectName("infwrong")
        self.gridLayout.addWidget(self.infwrong, 5, 0, 1, 1)
        self.appendbtn = QtWidgets.QPushButton(Form)
        self.appendbtn.setObjectName("appendbtn")
        self.gridLayout.addWidget(self.appendbtn, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить в прочитанное"))
        self.label.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Информация о книге</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Название книги:</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Автор книги:</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Жанр:</span></p></body></html>"))
        self.selectfile.setText(_translate("Form", "выбрать файл"))
        self.appendbtn.setText(_translate("Form", "добавить"))
