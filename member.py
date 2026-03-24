from book import Book

class Member:

    """
    This is the maximum amount of books a standard member can borrow all at once
    """
    max_books = 5 

    """
    Initializes member with their name and member_id, and creates an empty list of books they have borrowed.
    """
    def __init__(self, name, member_id):

        self.type = "Standard"
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    
    """
    This method:
    - takes a book class instance and checks if the member as hit their limit on books borrowed at once
    - then it checks if the book is availble by calling the method borrow() from the book class
    - if both return true then the book's isbn is added to member's borrowed books list (the isbn is added specifically because of the library class using isbn as a common identifier list their books, this allows it to be a universal indentifier for books accross different classes)
    - if the book isn't available then the borrowing process will fail and print an error message and the method will return False
    - if the member has reached their limit an error message will be printed and the method will return False
    """
    def borrow_book(self, book):
        if self.max_books > (len(self.borrowed_books)):
            
            if book.borrow(): 
                self.borrowed_books.append(book.isbn)
                return True
            
            else:
                print("Book not available")
                return False
        
        else:
            print('You have reached your limit for borrowed books, please return a book to borrow this one')
            return False

    
    """
    This returns a book specifed and removes the isbn from the list of borrowed books for that class' instance
    """
    def return_book(self, book):
        self.borrowed_books.remove(book.isbn)
        book.return_book()
    
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    
    def __str__(self):
        return 'Name: {} - ID: {}'.format(self.name, self.member_id)
    
    
    """
    This serializes the member object it is called upon into a dictionary type with all it's attributes, this method is also a reason why we use isbn in the borrowed_books list as to not return the object's memory address which would happen if it was stored as an object rather than an isbn
    """
    def serialization(self): 
        return self.__dict__
    



"""
This seperate class is for members who are student's, they are initialized with the class that it inherits (Member) but called through this subclass so that it assigns the type of Student as well as making the maximum books that can be borrowed at once 3 instead of 5.
"""
class StudentMember(Member):
    
    max_books = 3
    
    def __init__(self, name, member_id):
        
        super().__init__(name, member_id)
        self.type = "Student"




"""
This other sub class of Member is similar in functionality to the Student subclass however the type is changed from Standard to Faculty, the amount of books one can borrow at once also increases to 10.
"""
class FacultyMember(Member):
    
    max_books = 10
    
    def __init__(self, name, member_id):
        
        super().__init__(name, member_id)
        self.type = "Faculty"


