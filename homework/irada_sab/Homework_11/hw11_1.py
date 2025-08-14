# Создайте класс book с атрибутами:
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте (штук 5) экземпляров разных книг. После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# книга зарезервирована: Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если нет: Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага


class Book:
    page_material = 'paper'
    txt_presence = True

    def __init__(self, title, author, pages_count, isbn, reserved = False):
         self.title = title
         self.author = author
         self.pages_count = pages_count
         self.isbn = isbn
         self.reserved = reserved

    def __str__(self):
        reserved_status = ', Reserved' if self.reserved else ''
        return (f'Book name: {self.title}, Author: {self.author}, '
                f'Number of pages: {self.pages_count}, Material: {self.page_material}{reserved_status}')


book1 = Book('Idiot', 'Dostoevsky', 500, 'QWER-123')
book2 = Book('The Alchemist', 'P.Coelho', 200, 'ASD-456')
book3 = Book('The Financier', 'T.Drayzer', 570, 'ZXC-789')
book4 = Book('Harry Potter', 'J.K.Rowling', 700, 'WERT-234')
book5 = Book('Great Gatsby', 'S.Fitzgerald', 250, 'CVB-897')

book4.reserved = True

for book in [book1, book2, book3, book4, book5]:
    print(book)


# Создайте дочерний класс для первого. класс для школьных учебников. В нем будут доп атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервиров слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если нет: Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


class SchoolBook(Book):
    def __init__(self, title, author, pages_count, isbn, subject, grade, assignment, reserved = False):
        super().__init__(title, author, pages_count, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.assignment = assignment

    def __str__(self):
        reserved_schoolbook = ', Reserved' if self.reserved else ''
        return (f'Book name: {self.title}, Author: {self.author}, '
                f' Pages: {self.pages_count}, Subject: {self.subject}, Grade: {self.grade}{reserved_schoolbook}')


math_book = SchoolBook('Algebra', 'Kirov', 100, 'GGG-555', 'Math', 9, True)
language_book = SchoolBook('Spanish', 'Gonzales', 95, 'VVVV-999', 'Language', 11, False)
history_book = SchoolBook('USA history', 'J.Becker', 88, 'HHH-333', 'History', 10, False)

language_book.reserved = True

for book in [math_book, language_book, history_book]:
    print(book)
