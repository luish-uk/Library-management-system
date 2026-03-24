from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, book):
        if (book.isbn) not in self.books:
            self.books[book.isbn] = book
        else:
            return 'Error, this book has already been added'
    
    def remove_book(self, isbn):
        if (isbn) in self.books:
            del self.books[isbn]
        else: 
            return 'Error, this book doesn\'t exist'

    def register_member(self, member):
        if (member.member_id) not in self.members:
            self.members[member.member_id] = member
        else:
            return 'Error, this member already exists'

    def get_book(self, isbn):
        return self.books[isbn]

    def get_member(self, member_id):
        return self.members[member_id]
    
    def borrow_book(self, member_id, isbn):
        member = self.members[member_id] #Stores member object
        book = self.books[isbn] #Stores book object
        if book.borrow() == True and member.borrow_book(book) == True: #Calls both methods
            print("Success book as been borrowed - Library")
        else:
            print("Error book could not be borrowed - Library")

    def return_book(self, member_id, isbn):
        book = self.books[isbn]
        member = self.members[member_id]
        if book in member.borrowed_books:
            book.return_book()
            member.return_book(book)
            print("Success, book has been returned!")
        else:
            print("This member is not borrowing this book")
    
    def __str__(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())
        print("\nMembers:")
        for person in self.members:
            print(self.members[person].__str__())