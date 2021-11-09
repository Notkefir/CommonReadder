import sqlite3
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from first_for_proj import Ui_MainWindow
from about_programm import Ui_widget
from Library import Ui_form
from favourites import Ui_Form
from readlist import Ui_Widget
from inprocess import Ui_FOrm
from Append_book import Ui_FoRm
from Delete import Ui_ForM
from Read import Ui_FORM
from Append_favourite import UI_FOrm
from Delete_fav import UI_Form
from Append_readlist import UI_FORm
from Delete_readlist import UI_FORM
from Append_and_delete import UI_FoRM


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

        self.orig = Image.open(self.fname)
        self.orig_pixels = self.orig.load()
        self.im = Image.open(self.fname)
        self.a = ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.a)
        self.startpicture.setPixmap(self.pixmap)
        self.aboutProgramm.clicked.connect(self.about_programm)
        self.library.clicked.connect(self.about_library)
        self.favourites.clicked.connect(self.about_favourites)
        self.read.clicked.connect(self.about_read)
        self.inprocess.clicked.connect(self.about_process)

    def about_programm(self):
        self.second = AboutProgram()
        self.second.show()

    def about_library(self):
        self.third = library()
        self.third.show()

    def about_favourites(self):
        self.fourth = favourite()
        self.fourth.show()

    def about_read(self):
        self.fiveth = read()
        self.fiveth.show()

    def about_process(self):
        self.sixth = Inprocess()
        self.sixth.show()


class AboutProgram(QWidget, Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class library(QWidget, Ui_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.append.clicked.connect(self.about_append_books)
        self.pushButton_2.clicked.connect(self.about_delete_books)
        self.beginreadding.clicked.connect(self.about_readding_books)
        self.con = sqlite3.connect("llibrary.db")
        self.titles = None
        self.modified = []
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute('''SELECT Books.title,
       Authors.Author,
       genres.title
  FROM Books
       INNER JOIN
       genres ON Books.genre_id = genres.id
       INNER JOIN
       Authors ON Books.Authors_id = Authors.id;''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def about_append_books(self):
        self.appends = append_books()
        self.appends.show()

    def about_delete_books(self):
        self.deletes = delete_books()
        self.deletes.show()

    def about_readding_books(self):
        self.readding = Readding_books()
        self.readding.show()


class favourite(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.append2.clicked.connect(self.about_append_favourite_books)
        self.delete2.clicked.connect(self.about_delete_favourite_books)
        self.con = sqlite3.connect("llibrary.db")
        self.titles = None
        self.modified = []
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute('''SELECT Favourites.title,
               Authors.Author,
               genres.title
          FROM Favourites
               INNER JOIN
               genres ON Favourites.genre_id = genres.id
               INNER JOIN
               Authors ON Favourites.Authors_id = Authors.id;''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def about_append_favourite_books(self):
        self.appends2 = append_favourite_books()
        self.appends2.show()

    def about_delete_favourite_books(self):
        self.deletes2 = delete_favourites_books()
        self.deletes2.show()


class read(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.append3.clicked.connect(self.about_append_favourite_books)
        self.delete3.clicked.connect(self.about_delete_books)
        self.readappend.clicked.connect(self.about_append_books)
        self.con = sqlite3.connect("llibrary.db")
        self.titles = None
        self.modified = []
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute('''SELECT Readed.title,
                       Authors.Author,
                       genres.title
                  FROM Readed
                       INNER JOIN
                       genres ON Readed.genre_id = genres.id
                       INNER JOIN
                       Authors ON Readed.Authors_id = Authors.id;''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def about_append_books(self):
        self.appendreadlist = append_readlist()
        self.appendreadlist.show()

    def about_append_favourite_books(self):
        self.appends2 = append_favourite_books()
        self.appends2.show()

    def about_delete_books(self):
        self.deletes3 = delete_readlist()
        self.deletes3.show()


class Inprocess(QWidget, Ui_FOrm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.append4.clicked.connect(self.about_append_books)
        self.delete4.clicked.connect(self.about_delete_books)
        self.pushButton_3.clicked.connect(self.about_readding_books)
        self.con = sqlite3.connect("llibrary.db")
        self.titles = None
        self.modified = []
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute('''SELECT Books.title,
       genres.title,
       Authors.Author,
       link.way
  FROM inprocess
  left join link on link.id = inprocess.link_id
       LEFT JOIN
       Books ON Books.link_id = link.id
       LEFT JOIN
       genres ON Books.genre_id = genres.Id
       left join
       Authors ON Books.Authors_id = Authors.id''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def about_append_books(self):
        self.appends4 = append_favourite_books()
        self.appends4.show()

    def about_delete_books(self):
        self.deletes4 = append_and_del()
        self.deletes4.show()

    def about_readding_books(self):
        self.readdding = Readding_books()
        self.readdding.show()


class append_books(QWidget, Ui_FoRm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_lib)
        self.con = sqlite3.connect("llibrary.db")

    def append_book_lib(self):
        flag = True
        try:
            self.nameauth = self.authoredit.text()
            if not self.nameauth:
                self.authoredit.setText('no author')
                self.nameauth = 'no inf'
            self.titlebook = self.booknameedit.text()
            if not self.titlebook:
                self.infwrong.setText('no title')
                flag = False
            self.genre = self.genreedit.text()
            if not self.genre:
                self.genreedit.setText('no genre')
                self.genre = 'no inf'
            if not self.fnamebook:
                self.infwrong.setText('нет файла')
                flag = False
            if flag:
                cur = self.con.cursor()
                result = cur.execute('''select title from genres;''').fetchall()
                list_genres = [i[0].lower() for i in result]
                if self.genre.lower not in list_genres:
                    curr = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    curr.execute(que)
                    self.con.commit()
                currr = self.con.cursor()
                resultt = currr.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in resultt]
                if self.nameauth.lower not in list_authors:
                    currrr = self.con.cursor()
                    quee = f"insert into Authors(Author) values('{self.nameauth}')"
                    currrr.execute(quee)
                    self.con.commit()
                cuurrr = self.con.cursor()
                resuultt = cuurrr.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in resuultt]
                if self.fnamebook.lower not in list_links:
                    cuurrrr = self.con.cursor()
                    quuee = f"insert into link(way) values('{self.fnamebook}')"
                    cuurrrr.execute(quuee)
                    self.con.commit()
                currrrr = self.con.cursor()
                queee = f"""INSERT INTO Books (
                              Authors_id,
                              title,
                              genre_id,
                              link_id
                          )
                          VALUES (
                              (
                                  SELECT id
                                    FROM Authors
                                   WHERE Author = '{self.nameauth}'
                              ),
                              '{self.titlebook}',
                              (
                                  SELECT id
                                    FROM genres
                                   WHERE title = '{self.genre}'
                              ),
                              (
                                  SELECT id
                                    FROM link
                                   WHERE way = '{self.fnamebook}'
                              )
                          );"""
                currrrr.execute(queee)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


class delete_books(QWidget, Ui_ForM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delselfilebtn.clicked.connect(self.select_file)
        self.deletebtn.clicked.connect(self.delete_book_lib)
        self.con = sqlite3.connect("llibrary.db")

    def delete_book_lib(self):
        flag = True
        try:
            self.delaut = self.delautbtn.text()
            if not self.delaut:
                self.delwronglbl.setText('no author')
            self.delgenre = self.delgenrebtn.text()
            if not self.delgenre:
                self.delwronglbl.setText('no genre')
            self.deltitle = self.delbookbtn.text()
            if not self.deltitle:
                self.delwronglbl.setText('no title')
                flag = False
            if not self.fdelnamebook:
                self.delwronglblwrong.setText('нет файла')
                flag = False
            if flag:
                valid = QMessageBox.question(
                    self, '', "Действительно удалить элементы с id ", QMessageBox.Yes, QMessageBox.No)
                if valid == QMessageBox.Yes:
                    cur = self.con.cursor()
                    cur.execute(f"""DELETE FROM Books
              WHERE title = '{self.deltitle}' AND 
                    (
                SELECT id
                  FROM link
                 WHERE way = '{self.fdelnamebook}'
            );""")
                    self.con.commit()
        except Exception as e:
            self.delwronglbl.setText(str(e))

    def select_file(self):
        self.fdelnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                        initialFilter="Exes (*.txt )")[0]
        self.filenameedt.setText(self.fdelnamebook)


class Readding_books(QWidget, Ui_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openfbtn.clicked.connect(self.select_file)
        self.readbtn.clicked.connect(self.open_file)
        self.themebtn.clicked.connect(self.change_theme)
        self.con = sqlite3.connect("llibrary.db")

    def change_theme(self):
        if self.themebtn.text() == 'Тёмная':
            self.plainTextEdit.setStyleSheet("""
                                                QPlainTextEdit {background-color: #000000;}
                                                QPlainTextEdit {background-color:#000000} QPlainTextEdit {color:#FFFFFF}
                                                QPlainTextEdit {
                                                border-style: outset;
                                                border-width: 1px;
                                                border-color: #FFFFFF;} """)
            self.themebtn.setText("Светлая")
        elif self.themebtn.text() == 'Светлая':
            self.plainTextEdit.setStyleSheet("""
                                                QPlainTextEdit {background-color: #FFFFFF;}
                                                QPlainTextEdit {background-color:#FFFFFF} QPlainTextEdit {color:#000000}
                                                QPlainTextEdit {
                                                border-style: outset;
                                                border-width: 1px;
                                                border-color: #000000;} """)
            self.themebtn.setText("Тёмная")

    def open_file(self):
        flag = True
        try:
            self.title = self.titleedt.text()
            if not self.title:
                self.wronglbl.setText('введите название книги')
                flag = False
            self.file_name = self.fileedt.text()
            if not self.file_name:
                self.wronglbl.setText('выберите файл')
                flag = False
            if flag:
                currrrr = self.con.cursor()
                queee = f"""INSERT INTO inprocess (
                                              title,
                                              link_id
                                          )VALUES (
                                              '{self.title}',
                                              (
                                                  SELECT id
                                                    FROM link
                                                   WHERE way = '{self.file_name}'
                                              )
                                          );"""
                currrrr.execute(queee)
                self.con.commit()
                with open(self.file_name, 'r', encoding='UTF-8') as file:
                    self.plainTextEdit.setPlainText(file.read())
                    self.plainTextEdit.setReadOnly(True)
        except Exception as e:
            self.wronglbl.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.fileedt.setText(self.fnamebook)


class delete_favourites_books(QWidget, UI_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delselfilebtn.clicked.connect(self.select_file)
        self.deletebtn.clicked.connect(self.delete_book_fav)
        self.con = sqlite3.connect("llibrary.db")

    def delete_book_fav(self):
        flag = True
        try:
            self.deltitle = self.delbookbtn.text()
            if not self.deltitle:
                self.label_6.setText('no title')
                flag = False
            self.delaut = self.delautbtn.text()
            if not self.delaut:
                self.label_6.setText('no author')
            self.delgenre = self.delgenrebtn.text()
            if not self.delgenre:
                self.label_6.setText('no genre')
            if not self.fdelnamebook:
                self.label_6.setText('нет файла')
                flag = False
            if flag:
                valid = QMessageBox.question(
                    self, '', "Действительно удалить элементы с id ", QMessageBox.Yes, QMessageBox.No)
                if valid == QMessageBox.Yes:
                    cur = self.con.cursor()
                    cur.execute(f"""DELETE FROM Favourites
                      WHERE title = '{self.deltitle}' AND 
                            (
                        SELECT id
                          FROM link
                         WHERE way = '{self.fdelnamebook}'
                    );""")
                    self.con.commit()
        except Exception as e:
            self.label_6.setText(str(e))

    def select_file(self):
        self.fdelnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                        initialFilter="Exes (*.txt )")[0]
        self.filenameedt.setText(self.fdelnamebook)


class append_favourite_books(QWidget, UI_FOrm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_favourites)
        self.con = sqlite3.connect("llibrary.db")

    def append_book_favourites(self):
        flag = True
        try:
            self.nameauth = self.authoredit.text()
            if not self.nameauth:
                self.authoredit.setText('no author')
                self.nameauth = 'no inf'
            self.titlebook = self.booknameedit.text()
            if not self.titlebook:
                self.infwrong.setText('no title')
                flag = False
            self.genre = self.genreedit.text()
            if not self.genre:
                self.genreedit.setText('no genre')
                self.genre = 'no inf'
            if not self.fnamebook:
                self.infwrong.setText('нет файла')
                flag = False
            if flag:
                cur = self.con.cursor()
                result = cur.execute('''select title from genres;''').fetchall()
                list_genres = [i[0].lower() for i in result]
                if self.genre.lower not in list_genres:
                    curr = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    curr.execute(que)
                    self.con.commit()
                currr = self.con.cursor()
                resultt = currr.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in resultt]
                if self.nameauth.lower not in list_authors:
                    currrr = self.con.cursor()
                    quee = f"insert into Authors(Author) values('{self.nameauth}')"
                    currrr.execute(quee)
                    self.con.commit()
                cuurrr = self.con.cursor()
                resuultt = cuurrr.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in resuultt]
                if self.fnamebook.lower not in list_links:
                    cuurrrr = self.con.cursor()
                    quuee = f"insert into link(way) values('{self.fnamebook}')"
                    cuurrrr.execute(quuee)
                    self.con.commit()
                currrrr = self.con.cursor()
                queee = f"""INSERT INTO Favourites (
                              Authors_id,
                              title,
                              genre_id,
                              link_id
                          )
                          VALUES (
                              (
                                  SELECT id
                                    FROM Authors
                                   WHERE Author = '{self.nameauth}'
                              ),
                              '{self.titlebook}',
                              (
                                  SELECT id
                                    FROM genres
                                   WHERE title = '{self.genre}'
                              ),
                              (
                                  SELECT id
                                    FROM link
                                   WHERE way = '{self.fnamebook}'
                              )
                          );"""
                currrrr.execute(queee)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


class append_readlist(QWidget, UI_FORm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_favourites)
        self.con = sqlite3.connect("llibrary.db")

    def append_book_favourites(self):
        flag = True
        try:
            self.nameauth = self.authoredit.text()
            if not self.nameauth:
                self.authoredit.setText('no author')
                self.nameauth = 'no inf'
            self.titlebook = self.booknameedit.text()
            if not self.titlebook:
                self.infwrong.setText('no title')
                flag = False
            self.genre = self.genreedit.text()
            if not self.genre:
                self.genreedit.setText('no genre')
                self.genre = 'no inf'
            if not self.fnamebook:
                self.infwrong.setText('нет файла')
                flag = False
            if flag:
                cur = self.con.cursor()
                result = cur.execute('''select title from genres;''').fetchall()
                list_genres = [i[0].lower() for i in result]
                if self.genre.lower not in list_genres:
                    curr = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    curr.execute(que)
                    self.con.commit()
                currr = self.con.cursor()
                resultt = currr.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in resultt]
                if self.nameauth.lower not in list_authors:
                    currrr = self.con.cursor()
                    quee = f"insert into Authors(Author) values('{self.nameauth}')"
                    currrr.execute(quee)
                    self.con.commit()
                cuurrr = self.con.cursor()
                resuultt = cuurrr.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in resuultt]
                if self.fnamebook.lower not in list_links:
                    cuurrrr = self.con.cursor()
                    quuee = f"insert into link(way) values('{self.fnamebook}')"
                    cuurrrr.execute(quuee)
                    self.con.commit()
                currrrr = self.con.cursor()
                queee = f"""INSERT INTO Readed (
                              Authors_id,
                              title,
                              genre_id,
                              link_id
                          )
                          VALUES (
                              (
                                  SELECT id
                                    FROM Authors
                                   WHERE Author = '{self.nameauth}'
                              ),
                              '{self.titlebook}',
                              (
                                  SELECT id
                                    FROM genres
                                   WHERE title = '{self.genre}'
                              ),
                              (
                                  SELECT id
                                    FROM link
                                   WHERE way = '{self.fnamebook}'
                              )
                          );"""
                currrrr.execute(queee)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


class delete_readlist(QWidget, UI_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delselfilebtn.clicked.connect(self.select_file)
        self.deletebtn.clicked.connect(self.delete_book_lib)
        self.con = sqlite3.connect("llibrary.db")

    def delete_book_lib(self):
        flag = True
        try:
            self.delaut = self.delautbtn.text()
            if not self.delaut:
                self.label_6.setText('no author')
            self.deltitle = self.delbookbtn.text()
            if not self.deltitle:
                self.label_6.setText('no title')
                flag = False
            self.delgenre = self.delgenrebtn.text()
            if not self.delgenre:
                self.label_6.setText('no genre')
            if not self.fdelnamebook:
                self.label_6.setText('нет файла')
                flag = False
            if flag:
                valid = QMessageBox.question(
                    self, '', "Действительно удалить элементы с id ", QMessageBox.Yes, QMessageBox.No)
                if valid == QMessageBox.Yes:
                    cur = self.con.cursor()
                    cur.execute(f"""DELETE FROM Readed
                      WHERE title = '{self.deltitle}' AND 
                            (
                        SELECT id
                          FROM link
                         WHERE way = '{self.fdelnamebook}'
                    );""")
                    self.con.commit()
        except Exception as e:
            self.label_6.setText(str(e))

    def select_file(self):
        self.fdelnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                        initialFilter="Exes (*.txt )")[0]
        self.filenameedt.setText(self.fdelnamebook)


class append_and_del(QWidget, UI_FoRM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.delselfilebtn.clicked.connect(self.select_file)
        self.deletebtn.clicked.connect(self.delete_book_fav)
        self.con = sqlite3.connect("llibrary.db")

    def delete_book_fav(self):
        flag = True
        try:
            self.deltitle = self.delbookbtn.text()
            if not self.deltitle:
                self.label_6.setText('no title')
                flag = False
            self.delaut = self.delautbtn.text()
            if not self.delaut:
                self.label_6.setText('no author')
            self.delgenre = self.delgenrebtn.text()
            if not self.delgenre:
                self.label_6.setText('no genre')
            if not self.fdelnamebook:
                self.label_6.setText('нет файла')
                flag = False
            if flag:
                valid = QMessageBox.question(
                    self, '', "Действительно удалить элементы с id ", QMessageBox.Yes, QMessageBox.No)
                if valid == QMessageBox.Yes:
                    cur = self.con.cursor()
                    cur.execute(f"""DELETE FROM inprocess
                          WHERE title = '{self.deltitle}' AND 
                                (
                            SELECT id
                              FROM link
                             WHERE way = '{self.fdelnamebook}'
                        );""")
                    self.con.commit()
                    currrrr = self.con.cursor()
                    queee = f"""INSERT INTO Readed (
                                  Authors_id,
                                  title,
                                  genre_id,
                                  link_id
                              )
                              VALUES (
                                  (
                                      SELECT id
                                        FROM Authors
                                       WHERE Author = '{self.delaut}'
                                  ),
                                  '{self.deltitle}',
                                  (
                                      SELECT id
                                        FROM genres
                                       WHERE title = '{self.delgenre}'
                                  ),
                                  (
                                      SELECT id
                                        FROM link
                                       WHERE way = '{self.fdelnamebook}'
                                  )
                              );"""
                    currrrr.execute(queee)
                    self.con.commit()
        except Exception as e:
            self.label_6.setText(str(e))

    def select_file(self):
        self.fdelnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                        initialFilter="Exes (*.txt )")[0]
        self.filenameedt.setText(self.fdelnamebook)


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == "__main__":
    QApplication.setStyle('Breeze')
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
