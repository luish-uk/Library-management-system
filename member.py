from book import Book

class Member:
    max_books = 5
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if self.max_books > (len(self.borrowed_books)):
            if book.borrow():  
                self.borrowed_books.append(book)
            else:
                print('Book is not available')
        else:
            print('You have reached your limit for borrowed books, please return a book to borrow this one')

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def __str__(self):
        return 'Name: {}\nID: {}\nBorrowed: {}'.format(self.name, self.member_id, self.borrowed_books)
    
class StudentMember(Member):
    max_books = 3

class FacultyMember(Member):
    max_books = 10


