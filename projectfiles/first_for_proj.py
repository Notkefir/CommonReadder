# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_for_proj.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startpicture = QtWidgets.QLabel(self.centralwidget)
        self.startpicture.setGeometry(QtCore.QRect(110, 60, 201, 201))
        self.startpicture.setObjectName("startpicture")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 401, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aboutProgramm = QtWidgets.QPushButton(self.widget)
        self.aboutProgramm.setObjectName("aboutProgramm")
        self.horizontalLayout.addWidget(self.aboutProgramm)
        self.library = QtWidgets.QPushButton(self.widget)
        self.library.setObjectName("library")
        self.horizontalLayout.addWidget(self.library)
        self.favourites = QtWidgets.QPushButton(self.widget)
        self.favourites.setObjectName("favourites")
        self.horizontalLayout.addWidget(self.favourites)
        self.read = QtWidgets.QPushButton(self.widget)
        self.read.setObjectName("read")
        self.horizontalLayout.addWidget(self.read)
        self.inprocess = QtWidgets.QPushButton(self.widget)
        self.inprocess.setObjectName("inprocess")
        self.horizontalLayout.addWidget(self.inprocess)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startpicture.setText(_translate("MainWindow", "startpicture"))
        self.aboutProgramm.setText(_translate("MainWindow", "О программе"))
        self.library.setText(_translate("MainWindow", "Библиотека"))
        self.favourites.setText(_translate("MainWindow", "избранное"))
        self.read.setText(_translate("MainWindow", "прочитанное"))
        self.inprocess.setText(_translate("MainWindow", "В процессе"))
