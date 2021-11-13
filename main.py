import sqlite3
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from Designconvertedtopy import first_for_proj, about_programm, Library, favourites, readlist, inprocess, Append_book, \
    Delete, Read, Append_favourite, Delete_fav, Append_readlist, Delete_readlist, Append_and_delete, ProceedReading

"""Класс по открытию окна с информацией о программе"""


class MyWidget(QMainWindow, first_for_proj.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = 'C:/venv/project_qt/open-book.png'
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
        self.third = LibraryBooks()
        self.third.show()

    def about_favourites(self):
        self.fourth = FavouriteBooks()
        self.fourth.show()

    def about_read(self):
        self.fiveth = ReadBooks()
        self.fiveth.show()

    def about_process(self):
        self.sixth = Inprocess()
        self.sixth.show()


class AboutProgram(QWidget, about_programm.Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


"""класс для показа всех книг, которые есть"""


class LibraryBooks(QWidget, Library.Ui_form):
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
        result = cur.execute('''SELECT Books.title as 'название книги',
       Authors.Author as 'имя автора',
       genres.title as 'жанр', 
       link.way as 'путь'
  FROM Books
       INNER JOIN
       genres ON Books.genre_id = genres.id
       INNER JOIN
       Authors ON Books.Authors_id = Authors.id
       INNER JOIN
       link ON Books.link_id = link.id;''').fetchall()
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
        self.appends = AppendBooks()
        self.appends.show()

    def about_delete_books(self):
        self.deletes = DeleteBooks()
        self.deletes.show()

    def about_readding_books(self):
        self.readding = ReaddingBooks()
        self.readding.show()


"""Класс для показа избранных книг"""


class FavouriteBooks(QWidget, favourites.Ui_Form):
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
        result = cur.execute('''SELECT Favourites.title as 'название книги',
               Authors.Author as 'автор',
               genres.title as 'жанр',
               link.way as 'путь'
          FROM Favourites
               INNER JOIN
               genres ON Favourites.genre_id = genres.id
               INNER JOIN
               Authors ON Favourites.Authors_id = Authors.id
               INNER JOIN
               link ON Favourites.link_id = link.id;''').fetchall()
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
        self.appends2 = AppendFavouriteBooks()
        self.appends2.show()

    def about_delete_favourite_books(self):
        self.deletes2 = DeleteFavouritesBooks()
        self.deletes2.show()


"""класс для просмотра списка прочитанных книг"""


class ReadBooks(QWidget, readlist.Ui_Widget):
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
        result = cur.execute('''SELECT Readed.title as 'название книги',
                       Authors.Author as 'автор',
                       genres.title as 'жанр',
                       link.way as 'путь'
                  FROM Readed
                       INNER JOIN
                       genres ON Readed.genre_id = genres.id
                       INNER JOIN
                       Authors ON Readed.Authors_id = Authors.id
                       INNER JOIN
                       link ON Readed.link_id = link.id;''').fetchall()
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
        self.appendreadlist = AppendReadlist()
        self.appendreadlist.show()

    def about_append_favourite_books(self):
        self.appends2 = AppendFavouriteBooks()
        self.appends2.show()

    def about_delete_books(self):
        self.deletes3 = DeleteReadlist()
        self.deletes3.show()


"""класс для просмотра книг, которые в процессе"""


class Inprocess(QWidget, inprocess.Ui_FOrm):
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
        self.appends4 = AppendFavouriteBooks()
        self.appends4.show()

    def about_delete_books(self):
        self.deletes4 = AppendandDel()
        self.deletes4.show()

    def about_readding_books(self):
        self.readdding = ContinueReading()
        self.readdding.show()


"""класс по добавлению книг в общий список"""


class AppendBooks(QWidget, Append_book.Ui_FoRm):
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
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in result2]
                if self.nameauth.lower not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                result3 = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in result3]
                if self.fnamebook.lower not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                cur7 = self.con.cursor()
                que4 = f"""INSERT INTO Books (
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
                cur7.execute(que4)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


"""класс для удаления книг из общего списка книг"""


class DeleteBooks(QWidget, Delete.Ui_ForM):
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
                    self, '', "Действительно удалить эту книгу? ", QMessageBox.Yes, QMessageBox.No)
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


"""класс для чтения самой книги"""


class ReaddingBooks(QWidget, Read.Ui_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openfbtn.clicked.connect(self.select_file)
        self.readbtn.clicked.connect(self.open_file)
        self.themebtn.clicked.connect(self.change_theme)
        self.con = sqlite3.connect("llibrary.db")
        self.comboBox.activated[str].connect(self.onActivated)
        self.size = "8"

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

    def open_file(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT Books.title,
       link.way
  FROM Books
       INNER JOIN
       link ON Books.link_id = link.id;''').fetchall()
        cur2 = self.con.cursor()
        result2 = cur2.execute('''SELECT Inprocess.title,
               link.way
          FROM Inprocess
               INNER JOIN
               link ON Inprocess.link_id = link.id;''').fetchall()
        list_of_lways = [i[1] for i in result2]
        flag = True
        try:
            self.title = self.titleedt.text()
            self.file_name = self.fileedt.text()
            tit_and_fname = (self.title, self.file_name)
            if not self.title:
                self.wronglbl.setText('введите корректно название книги')
                flag = False
            if not self.file_name:
                self.wronglbl.setText('выберите корректно файл')
                flag = False
            if tit_and_fname not in result:
                self.wronglbl.setText('такой книги нет')
                flag = False
            if self.file_name in list_of_lways:
                self.wronglbl.setText('вы уже читаете её')
                flag = False
            if flag:
                self.wronglbl.setText('')
                cur3 = self.con.cursor()
                que3 = f"""INSERT INTO inprocess (
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
                cur3.execute(que3)
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

    def onActivated(self, text):
        if not text:
            text = '10'
        self.size = text
        self.plainTextEdit.setFont(QtGui.QFont("Times", int(self.size), QtGui.QFont.Bold))


"""класс по удалению книг из списка избранное"""


class DeleteFavouritesBooks(QWidget, Delete_fav.UI_Form):
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
                    self, '', "Действительно удалить эту книгу? ", QMessageBox.Yes, QMessageBox.No)
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


"""класс для добавления книг в список избранное"""


class AppendFavouriteBooks(QWidget, Append_favourite.UI_FOrm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_favourites)
        self.con = sqlite3.connect("llibrary.db")

    def append_book_favourites(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT Inprocess.title, link.way
                  FROM Inprocess
                       INNER JOIN
                       link ON Inprocess.link_id = link.id;''').fetchall()
        list_of_lways = [i[1] for i in result]
        cur2 = self.con.cursor()
        result2 = cur2.execute('''SELECT Books.title,
               link.way
          FROM Books
               INNER JOIN
               link ON Books.link_id = link.id;''').fetchall()
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
            if self.fnamebook in list_of_lways:
                self.infwrong.setText('такая книга уже в списке')
                flag = False
            if (self.titlebook, self.fnamebook) not in result2:
                self.infwrong.setText('такой книги нет в библиотеке')
                flag = False
            if flag:
                cur = self.con.cursor()
                result = cur.execute('''select title from genres;''').fetchall()
                list_genres = [i[0].lower() for i in result]
                if self.genre.lower not in list_genres:
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in result2]
                if self.nameauth.lower not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                resuultt = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in resuultt]
                if self.fnamebook.lower not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                cur7 = self.con.cursor()
                que4 = f"""INSERT INTO Favourites (
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
                cur7.execute(que4)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


"""класс для добавления книг в прочитанное"""


class AppendReadlist(QWidget, Append_readlist.UI_FORm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_readlist)
        self.con = sqlite3.connect("llibrary.db")

    def append_book_readlist(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT Readed.title, link.way
                          FROM Readed
                               INNER JOIN
                               link ON Readed.link_id = link.id;''').fetchall()
        list_of_lways = [i[1] for i in result]
        cur2 = self.con.cursor()
        result2 = cur2.execute('''SELECT Books.title,
                       link.way
                  FROM Books
                       INNER JOIN
                       link ON Books.link_id = link.id;''').fetchall()
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
            if self.fnamebook in list_of_lways:
                self.infwrong.setText('такая книга уже в списке')
                flag = False
            if (self.titlebook, self.fnamebook) not in result2:
                self.infwrong.setText('такой книги нет в библиотеке')
                flag = False
            if flag:
                cur = self.con.cursor()
                result = cur.execute('''select title from genres;''').fetchall()
                list_genres = [i[0].lower() for i in result]
                if self.genre.lower not in list_genres:
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower for i in result2]
                if self.nameauth.lower not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                resuultt = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower for i in resuultt]
                if self.fnamebook.lower not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                cur7 = self.con.cursor()
                que4 = f"""INSERT INTO Readed (
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
                cur7.execute(que4)
                self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)


"""класс для удления книг из списка прочитанное"""


class DeleteReadlist(QWidget, Delete_readlist.UI_FORM):
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
                    self, '', "Действительно удалить эту книгу ", QMessageBox.Yes, QMessageBox.No)
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


"""класс для завершения чтения книги и добавления его в прочитанное"""


class AppendandDel(QWidget, Append_and_delete.UI_FoRM):
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
                    self, '', "Действительно удалить эту книгу", QMessageBox.Yes, QMessageBox.No)
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
                    cur2 = self.con.cursor()
                    que = f"""INSERT INTO Readed (
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
                    cur2.execute(que)
                    self.con.commit()
        except Exception as e:
            self.label_6.setText(str(e))

    def select_file(self):
        self.fdelnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                        initialFilter="Exes (*.txt )")[0]
        self.filenameedt.setText(self.fdelnamebook)
class ContinueReading(QWidget, ProceedReading.UI_FoRm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openfbtn.clicked.connect(self.select_file)
        self.readbtn.clicked.connect(self.open_file)
        self.themebtn.clicked.connect(self.change_theme)
        self.con = sqlite3.connect("llibrary.db")
        self.comboBox.activated[str].connect(self.onActivated)
        self.size = "8"

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

    def open_file(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT Inprocess.title,
                 link.way
            FROM Inprocess
                 INNER JOIN
                 link ON Inprocess.link_id = link.id;''').fetchall()
        flag = True
        try:
            self.title = self.titleedt.text()
            self.file_name = self.fileedt.text()
            tit_and_fname = (self.title, self.file_name)
            if not self.title:
                self.wronglbl.setText('введите корректно название книги')
                flag = False
            if not self.file_name:
                self.wronglbl.setText('выберите корректно файл')
                flag = False
            if tit_and_fname not in result:
                self.wronglbl.setText('такой книги нет')
                flag = False
            if flag:
                self.wronglbl.setText('')
                with open(self.file_name, 'r', encoding='UTF-8') as file:
                    self.plainTextEdit.setPlainText(file.read())
                    self.plainTextEdit.setReadOnly(True)

        except Exception as e:
            self.wronglbl.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.fileedt.setText(self.fnamebook)

    def onActivated(self, text):
        if not text:
            text = '10'
        self.size = text
        self.plainTextEdit.setFont(QtGui.QFont("Times", int(self.size), QtGui.QFont.Bold))

def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == "__main__":
    QApplication.setStyle('Breeze')
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
