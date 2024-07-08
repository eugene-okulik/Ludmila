class Book:
   material = "бумага"
   has_text = True

   def __init__(self, title, author, pages):
       self.title = title
       self.author = author
       self.pages = pages
       self.reserved = False

   def reserve(self):
       self.reserved = True

   def __str__(self):
        return f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}'.strip()


class School(Book):

    def __init__(self, title, author, pages, subject, group, task=True):
        super().__init__(title, author, pages)
        self.subject = subject
        self.group = group
        self.task = task

    def __str__(self):
        reserve_status = ', зарезервирована' if self.reserved else ''
        return (f'Название: {self.title}, Автор: {self.author}, страниц: {self.pages}, '
                f'предмет: {self.subject}, класс: {self.group}{reserve_status}').strip()


book_one = School('Aлгебра', 'Иванов', 500, 'Математика', 5, True)
book_two = School('История', 'Петров', 200, 'История', 8, False)
book_three = School('География', 'Сидоров', 350, 'География', 8, False)
book_four = School('Биология', 'Марков', 400, 'Биология', 9, True)
book_five = School('Физика', 'Петров', 280, 'Физика', 10, True)

book_four.reserve()

books = [book_one, book_two, book_three, book_four, book_five]
for book in books:
    print(book)
