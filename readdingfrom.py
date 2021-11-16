import sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget
from Designconvertedtopy import Read

class ReaddingBooks(QWidget, Read.Ui_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.themebtn.clicked.connect(self.change_theme)
        self.con = sqlite3.connect("llibrary.db")
        self.comboBox.activated[str].connect(self.onactivated)
        self.size = "8"
        self.f_name = None
        self.plainTextEdit.setReadOnly(True)
        self.themebtn.setText('Тёмная')

    def change_theme(self):
        if self.themebtn.text() == 'Тёмная':
            self.plainTextEdit.setStyleSheet("""
                                                QPlainTextEdit {background-color: #000000;}
                                                QPlainTextEdit {background-color:#000000} QPlainTextEdit {color:#FFFFFF}
                                                QPlainTextEdit {
                                                border-style: outset;
                                                border-width: 1px;
                                                border-color: #FFFFFF;}""")
            self.themebtn.setText("Светлая")
        elif self.themebtn.text() == 'Светлая':
            self.plainTextEdit.setStyleSheet("""
                                                QPlainTextEdit {background-color: #FFFFFF;}
                                                QPlainTextEdit {background-color:#FFFFFF} QPlainTextEdit {color:#000000}
                                                QPlainTextEdit {
                                                border-style: outset;
                                                border-width: 1px;
                                                border-color: #000000;}""")
            self.themebtn.setText("Тёмная")

    def open_file(self, fname):
        self.f_name = fname
        with open(self.f_name, 'r', encoding='UTF-8') as file:
            try:
                self.plainTextEdit.setPlainText(file.read())
                self.plainTextEdit.setReadOnly(True)
            except Exception as e:
                print(e)

    def onactivated(self, text):
        if not text:
            text = '10'
        self.size = text
        self.plainTextEdit.setFont(QtGui.QFont("Times", int(self.size), QtGui.QFont.Bold))