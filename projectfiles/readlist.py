# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readlist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(363, 289)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.append3 = QtWidgets.QPushButton(widget)
        self.append3.setObjectName("append3")
        self.gridLayout.addWidget(self.append3, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 3)
        self.delete3 = QtWidgets.QPushButton(widget)
        self.delete3.setObjectName("delete3")
        self.gridLayout.addWidget(self.delete3, 1, 2, 1, 1)
        self.readappend = QtWidgets.QPushButton(widget)
        self.readappend.setObjectName("readappend")
        self.gridLayout.addWidget(self.readappend, 1, 1, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Прочитанное"))
        self.append3.setText(_translate("widget", "В избранное"))
        self.delete3.setText(_translate("widget", "Удалить из прочитанного"))
        self.readappend.setText(_translate("widget", "добавить"))
