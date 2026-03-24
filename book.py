

class Book:
    
    books = 0

    books_borrowed = 0

    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.is_available = True
        Book.books += 1
        Book.members.append(self)
    def borrow(self):
        if self.is_available:
            self.is_available = False
            Book.books_borrowed += 1
            return 'Successfully borrowed book'
        else:
            return 'Error, book is not available'

    @classmethod
    def supply(cls):
        return 'We have {} books available, and {} books being borrowed.'.format((cls.books - cls.books_borrowed), cls.books_borrowed)
    
    @classmethod
    def number_of_books(cls):
        return 'We have a total of {} books.'.format(cls.books)

    def get_info(self):
        return print(self.__dict__)
    

    def return_book(self):
        self.is_available = True
        Book.books_borrowed -= 1
        return 'Successfully returned book'
    
    def __str__(self):
        return '{} by {}, book available: {}.'.format(self.title, self.author, self.is_available)
    

book1 = Book("Atomic Habits", "James Clear", 9780735211292)

print(book1.get_info())
print(book1.borrow())

print(Book.supply())

print(book1.borrow())
print(book1.return_book())
print(book1.__str__())

print(Book.number_of_books())
print(Book.supply())