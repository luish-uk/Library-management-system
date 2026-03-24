from book import Book

class Member:
    max_books = 5
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if self.max_books > (len(self.borrowed_books)):
            if book.borrow():  # Check if book is available
                self.borrowed_books.append(book)
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
        for item in self.borrowed_books:
            print(item.__str__())
    
    def __str__(self):
        return 'Name: {} - ID: {}'.format(self.name, self.member_id)
    
class StudentMember(Member):
    max_books = 3

class FacultyMember(Member):
    max_books = 10


