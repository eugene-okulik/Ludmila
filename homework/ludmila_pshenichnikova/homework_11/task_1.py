class Book:
    material = 'бумага'
    has_text = True

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        self.reserved = True

    def __str__(self):
        reserve_status = 'зарезервирована' if self.reserved else ''
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'материал: {self.material} {reserve_status}')


book1 = Book('Война и мир', 'Толстой', 1500, '123-4567890124')
book2 = Book('Война и мир', 'Толстой', 1200, '123-4567890124')
book3 = Book('Преступление и наказание', 'Достоевский', 670, '123-4567890125')
book4 = Book('Мастер и Маргарита', 'Булгаков', 450, '123-4567890126')
book5 = Book('Анна Каренина', 'Толстой', 864, '123-4567890127')

book3.reserved = True

books = [book1, book2, book3, book4, book5]
for book in books:
    print(book)
