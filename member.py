from book import Book

class Member:
    max_books = 5
    def __init__(self, name, member_id):
        self.type = "Standard"
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if self.max_books > (len(self.borrowed_books)):
            if book.borrow():  # Check if book is available
                self.borrowed_books.append(book.isbn)
                return True
            else:
                print("Book not available")
                return False
        else:
            print('You have reached your limit for borrowed books, please return a book to borrow this one')
            return False

    def return_book(self, book):
        self.borrowed_books.remove(book)
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def __str__(self):
        return 'Name: {} - ID: {}'.format(self.name, self.member_id)
    
    def serialization(self): 
        return self.__dict__
    
class StudentMember(Member):
    max_books = 3
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.type = "Student"

class FacultyMember(Member):
    max_books = 10
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.type = "Faculty"


