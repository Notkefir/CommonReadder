import sqlite3
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QMainWindow

import readdingfrom
from Designconvertedtopy import first_for_proj, about_programm, Append_book, \
    Append_favourite, Append_readlist, Readertab, information


class MyWidget(QMainWindow, first_for_proj.Ui_CommonReader):
    """стартовое окно"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fname = 'project_qt/open-book.png'
        self.orig = Image.open(self.fname)
        self.orig_pixels = self.orig.load()
        self.im = Image.open(self.fname)
        self.a = ImageQt(self.im)
        self.pixmap = QPixmap.fromImage(self.a)
        self.startpicture.setPixmap(self.pixmap)
        self.startbtn.clicked.connect(self.start_program)

    def about_programm(self):
        self.second = AboutProgram()
        self.second.show()

    def start_program(self):
        self.third = Tabs()
        self.third.show()
        self.close()


class AboutProgram(QWidget, about_programm.Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Tabs(QWidget, Readertab.UI_formtab):
    """основной класс, содержащий всю информацию"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.appendlib.clicked.connect(self.append_lib_show)
        self.deletelib.clicked.connect(self.delete_lib)
        self.beginreadding.clicked.connect(self.open_book)
        self.appendfav.clicked.connect(self.append_fav_show)
        self.deletefav.clicked.connect(self.delete_fav)
        self.appendraed.clicked.connect(self.append_readlist_show)
        self.deleteread.clicked.connect(self.delete_readlist)
        self.appendtofav.clicked.connect(self.append_fav)
        self.comboBox.activated[str].connect(self.onActivatedlib)
        self.favcomboBox.activated[str].connect(self.onActivatedfav)
        self.readcomboBox.activated[str].connect(self.onActivatedread)
        self.update_table.clicked.connect(self.updatetables)
        self.option = ''
        self.con = sqlite3.connect("llibrary.db")
        self.titles = None
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
            self.libtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.libtableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.libtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.libtableWidget.setItem(i, j, QTableWidgetItem(str(val)))
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
            self.favtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.favtableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.favtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.favtableWidget.setItem(i, j, QTableWidgetItem(str(val)))
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
            self.readtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.readtableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.readtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.readtableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def append_lib_show(self):
        """добавление в общую библиотеку"""
        self.append_window = AppendBooks()
        self.append_window.show()

    def delete_lib(self):
        """удаление из общей библиотеки"""
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.libtableWidget.selectedItems()]))
        ids = [self.libtableWidget.item(i, 3).text() for i in rows]
        print(ids)
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        # Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute(
                "delete from Books where Books.link_id in (select link_id from link where link.way in (" + ", ".join(
                    '?' * len(ids)) + ")"")", ids)
            self.con.commit()

    def append_fav(self):
        """добавление в избранное"""
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.readtableWidget.selectedItems()]))
        way = [self.readtableWidget.item(i, 3).text() for i in rows]
        bookname = [self.readtableWidget.item(i, 0).text() for i in rows]
        auth = [self.readtableWidget.item(i, 1).text() for i in rows]
        genre = [self.readtableWidget.item(i, 2).text() for i in rows]
        print(bookname)
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно добавить элементы",
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        # Не забываем зафиксировать изменения
        try:
            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                for i in range(len(way)):
                    print(1)
                    cur.execute(f"""INSERT INTO Favourites (
                                      Authors_id,
                                      title,
                                      genre_id,
                                      link_id
                                  )
                                  VALUES (
                                      (
                                          SELECT id
                                            FROM Authors
                                           WHERE Author = '{auth[i]}'
                                      ),
                                      '{bookname[i]}',
                                      (
                                          SELECT id
                                            FROM genres
                                           WHERE title = '{genre[i]}'
                                      ),
                                      (
                                          SELECT id
                                            FROM link
                                           WHERE way = '{way[i]}'
                                      )
                                  );""")
                self.con.commit()
        except Exception as e:
            self.infwrong = Dialog()
            self.infwrong.show()

    def append_fav_show(self):
        """добавление из саммого избранное"""
        self.append_fav = AppendFavouriteBooks()
        self.append_fav.show()

    def delete_fav(self):
        """удаление из избрнного"""
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.favtableWidget.selectedItems()]))
        ids = [self.favtableWidget.item(i, 3).text() for i in rows]
        print(ids)
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        # Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute(
                "delete from Favourites where Favourites.link_id in (select link_id from link where link.way in (" + ", ".join(
                    '?' * len(ids)) + ")"")", ids)
            self.con.commit()

    def append_readlist_show(self):
        """добавление в список прочтенных"""
        self.append_read = AppendReadlist()
        self.append_read.show()

    def delete_readlist(self):
        """удаление из списка прочтенных"""
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.readtableWidget.selectedItems()]))
        ids = [self.readtableWidget.item(i, 3).text() for i in rows]
        print(ids)
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        # Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute(
                "delete from Favourites where Favourites.link_id in (select link_id from link where link.way in (" + ", ".join(
                    '?' * len(ids)) + ")"")", ids)
            self.con.commit()

    def onActivatedlib(self, text):
        """сортировка библиотеки"""
        cur = self.con.cursor()
        if text == 'сортировка по':
            self.option = "''"
        else:
            if text == 'Жанр':
                self.option = 'genres.title'
            elif text == 'Название книги':
                self.option = 'Books.title'
            elif text == 'Автор':
                self.option = 'Authors.Author'
        print(self.option)
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute(f'''SELECT Books.title,
                       genres.title,
                       Authors.Author,
                       link.way
                  FROM Books
                  left join link on link.id = Books.link_id
                       LEFT JOIN
                       genres ON Books.genre_id = genres.Id
                       left join
                       Authors ON Books.Authors_id = Authors.id
                       order by {self.option}''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.libtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.libtableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.libtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.libtableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def onActivatedfav(self, text):
        """сортировка  избранного"""
        cur = self.con.cursor()
        if text == 'сортировка по':
            self.option = "''"
        else:
            if text == 'Жанр':
                self.option = 'genres.title'
            elif text == 'Название книги':
                self.option = 'Favourites.title'
            elif text == 'Автор':
                self.option = 'Authors.Author'
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute(f'''SELECT Favourites.title,
                       genres.title,
                       Authors.Author,
                       link.way
                  FROM Favourites
                  left join link on link.id = Favourites.link_id
                       LEFT JOIN
                       genres ON Favourites.genre_id = genres.Id
                       left join
                       Authors ON Favourites.Authors_id = Authors.id
                       order by {self.option}''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.favtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.favtableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.favtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.favtableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def onActivatedread(self, text):
        """сортировка прочитанного"""
        cur = self.con.cursor()
        if text == 'сортировка по':
            self.option = "''"
        else:
            if text == 'Жанр':
                self.option = 'genres.title'
            elif text == 'Название книги':
                self.option = 'Readed.title'
            elif text == 'Автор':
                self.option = 'Authors.Author'
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute(f'''SELECT Readed.title,
                       genres.title,
                       Authors.Author,
                       link.way
                  FROM Readed
                  left join link on link.id = Readed.link_id
                       LEFT JOIN
                       genres ON Readed.genre_id = genres.Id
                       left join
                       Authors ON Readed.Authors_id = Authors.id
                       order by {self.option}''').fetchall()
        # Заполнили размеры таблицы
        if result:
            self.readtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.readtableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.readtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.readtableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def open_book(self):
        """взов класса ля чтения файла"""
        rows = list(set([i.row() for i in self.libtableWidget.selectedItems()]))
        ids = [self.libtableWidget.item(i, 3).text() for i in rows]
        fname = ids[0]
        self.open_file = readdingfrom.ReaddingBooks()
        self.open_file.open_file(fname)
        self.open_file.show()

    def updatetables(self):
        """обновление результата"""
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
            self.libtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.libtableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.libtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.libtableWidget.setItem(i, j, QTableWidgetItem(str(val)))
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
            self.favtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.favtableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            self.favtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.favtableWidget.setItem(i, j, QTableWidgetItem(str(val)))
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
            self.readtableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.readtableWidget.setColumnCount(len(result[0]))
            self.modified = result[0]
            self.titles = [description[0] for description in cur.description]
            self.readtableWidget.setHorizontalHeaderLabels(self.titles)
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.readtableWidget.setItem(i, j, QTableWidgetItem(str(val)))


class AppendBooks(QWidget, Append_book.Ui_FoRm):
    """добавление книги"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_lib)
        self.con = sqlite3.connect("llibrary.db")
        cur = self.con.cursor()
        self.genres = cur.execute('''select title from genres;''').fetchall()
        for i in self.genres:
            self.comboBox.addItem(i[0])
        self.comboBox.activated[str].connect(self.onActivated)
        self.genreedit.setPlaceholderText('жанр, если его нет в выпад. спсиске')
        self.genre = ''

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
            if not self.genre:
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
                if self.genre.lower() not in list_genres:
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre.lower()}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower() for i in result2]
                if self.nameauth.lower() not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                result3 = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower() for i in result3]
                if self.fnamebook.lower() not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                print(self.genre)
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

    def onActivated(self, text):
        self.genre = text


class AppendFavouriteBooks(QWidget, Append_favourite.UI_FOrm):
    """добавление книги в избранное"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_favourites)
        self.con = sqlite3.connect("llibrary.db")
        cur = self.con.cursor()
        self.genres = cur.execute('''select title from genres;''').fetchall()
        for i in self.genres:
            self.comboBox.addItem(i[0])
        self.comboBox.activated[str].connect(self.onActivated)
        self.genreedit.setPlaceholderText('жанр, если его нет в выпад. спсиске')
        self.genre = ''

    def append_book_favourites(self):
        cur2 = self.con.cursor()
        self.result2 = cur2.execute('''SELECT Books.title,
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
            if not self.genre:
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
                if self.genre.lower() not in list_genres:
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre.lower()}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower() for i in result2]
                if self.nameauth.lower() not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                result3 = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower() for i in result3]
                if self.fnamebook.lower() not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                print(self.genre)
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
                if (self.nameauth, self.fnamebook) not in self.result2:
                    cur8 = self.con.cursor()
                    que5 = f"""INSERT INTO Books (
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
                    cur8.execute(que5)
                    self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)

    def onActivated(self, text):
        self.genre = text


"""класс для добавления книг в прочитанное"""


class AppendReadlist(QWidget, Append_readlist.UI_FORm):
    """добавление в прочитанное"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectfile.clicked.connect(self.select_file)
        self.appendbtn.clicked.connect(self.append_book_favourites)
        self.con = sqlite3.connect("llibrary.db")
        cur = self.con.cursor()
        self.genres = cur.execute('''select title from genres;''').fetchall()
        for i in self.genres:
            self.comboBox.addItem(i[0])
        self.comboBox.activated[str].connect(self.onActivated)
        self.genreedit.setPlaceholderText('жанр, если его нет в выпад. спсиске')
        self.genre = ''

    def append_book_favourites(self):
        cur2 = self.con.cursor()
        self.result2 = cur2.execute('''SELECT Books.title,
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
            if not self.genre:
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
                if self.genre.lower() not in list_genres:
                    cur2 = self.con.cursor()
                    que = f"insert into genres(title) values('{self.genre.lower()}');"
                    cur2.execute(que)
                    self.con.commit()
                cur3 = self.con.cursor()
                result2 = cur3.execute('''select Author from Authors;''').fetchall()
                list_authors = [(i[0]).lower() for i in result2]
                if self.nameauth.lower() not in list_authors:
                    cur4 = self.con.cursor()
                    que2 = f"insert into Authors(Author) values('{self.nameauth}')"
                    cur4.execute(que2)
                    self.con.commit()
                cur5 = self.con.cursor()
                result3 = cur5.execute('''select way from link;''').fetchall()
                list_links = [(i[0]).lower() for i in result3]
                if self.fnamebook.lower() not in list_links:
                    cur6 = self.con.cursor()
                    que3 = f"insert into link(way) values('{self.fnamebook}')"
                    cur6.execute(que3)
                    self.con.commit()
                print(self.genre)
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
                if (self.nameauth, self.fnamebook) not in self.result2:
                    cur8 = self.con.cursor()
                    que5 = f"""INSERT INTO Books (
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
                    cur8.execute(que5)
                    self.con.commit()
        except Exception as e:
            self.infwrong.setText(str(e))

    def select_file(self):
        self.fnamebook = QFileDialog.getOpenFileName(self, filter="All (*);;Exes (*.txt )",
                                                     initialFilter="Exes (*.txt )")[0]
        self.filenameedit.setText(self.fnamebook)

    def onActivated(self, text):
        self.genre = text


class Dialog(QWidget, information.Ui_Dialog):
    """оповещение об ошибке пользователя"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('ранее вы добавляли такую книгу')


def except_hook(cls, exception, traceback):
    sys.excepthook(cls, exception, traceback)


if __name__ == "__main__":
    QApplication.setStyle('Breeze')
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
