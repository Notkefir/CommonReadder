# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favourites.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.append2 = QtWidgets.QPushButton(Form)
        self.append2.setObjectName("append2")
        self.gridLayout.addWidget(self.append2, 1, 0, 1, 1)
        self.delete2 = QtWidgets.QPushButton(Form)
        self.delete2.setObjectName("delete2")
        self.gridLayout.addWidget(self.delete2, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Favourites"))
        self.append2.setText(_translate("Form", "Добавить"))
        self.delete2.setText(_translate("Form", "Удалить"))