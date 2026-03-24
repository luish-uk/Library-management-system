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
        borrower = self.members[member_id] #Stores member object
        book = self.books[isbn] #Stores book object
        if borrower.borrow_book(book) == True: 
            print("Success book as been borrowed - Library")
        else:
            print("Error book could not be borrowed - Library")

    def return_book(self, member_id, isbn):
        book = self.books[isbn]
        returner = self.members[member_id]
        if book in returner.borrowed_books:
            book.return_book()
            returner.return_book(book)
            print("Success, book has been returned!")
        else:
            print("This member is not borrowing this book")

    def search_books(self, query): 
        print(f"\nSearch Results for '{query}':")
        results = 0 #List of results
        length = len(query) #length of query 
        for item in self.books:
            result = self.books[item] #grabs book objects
            title = result.title 
            author = result.author
            if query.upper() == title[:length].upper(): #does query match the first characters (=length) of the books (title/author)
                print(result.__str__())
                results += 1
            if query.upper() == author[:length].upper():
                print(result.__str__())
                results += 1
        if results == 0:
            print("Unable to find results from query")

    def list_all_books(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())
    
    def list_available_books(self):
        print("\nAvailable Books:")
        for item in self.books:
            item = self.books[item]
            if item.is_available:
                print(item.__str__())

    def list_member_books(self, member_id=None):
        if member_id is None:
            for person in self.members:
                person = self.members[person]
                print(f"\n{person.name}:")
                person.get_borrowed_books()
        else:
            person = self.members[member_id]
            print(f"\n{person.name}:")
            person.get_borrowed_books()
    
    def __str__(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())
        print("\nMembers:")
        for person in self.members:
            print(self.members[person].__str__())

    