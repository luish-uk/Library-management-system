from book import Book
from member import Member, StudentMember, FacultyMember
import json

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
    
    def borrow_book(self, member_id, isbn):#if key error 1 appears add the book first
        borrower = self.members[member_id] #Stores member object 
        book = self.books[isbn] #Stores book object
        if borrower.borrow_book(book) == True: 
            print("Success book as been borrowed - Library")
        else:
            print("Error book could not be borrowed - Library")

    def return_book(self, member_id, isbn):
        book = self.books[isbn] 
        returner = self.members[member_id]
        if isbn in returner.borrowed_books:
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
                booklist = person.get_borrowed_books()
                for ISBN in booklist:
                    book = self.books[ISBN]
                    print(book)
        else:
            person = self.members[member_id]
            print(f"\n{person.name}:")
            booklist = person.get_borrowed_books()
            for ISBN in booklist:
                book = self.books[ISBN]
                print(book)

    
    def __str__(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())
        print("\nMembers:")
        for person in self.members:
            print(self.members[person].__str__())

    def serialization(self):
        with open("Library.json", 'w') as file:
            serializedlibrary = {"books": [], "members": []}
            for item in self.books:
                serializedbook = self.books[item].serialization()
                serializedlibrary["books"].append(serializedbook)
            for id in self.members:
                serializedmember = self.members[id].serialization()
                serializedlibrary["members"].append(serializedmember)
            json.dump(serializedlibrary, file, indent = 4)
    def deserialization(self):
        with open("Library.json", "r") as file:
            data = json.load(file)

            self.books = {}
            self.members = {}



            for book_data in data["books"]:
                book = Book(book_data["title"], book_data["author"], book_data["isbn"])
                book.is_available = book_data["is_available"]
                self.books[book.isbn] = book

            for member_data in data["members"]:
                if member_data["type"] == "Student":
                    memberdeserialized = StudentMember(member_data["name"], member_data["member_id"])
                elif member_data["type"] == "Faculty":
                    memberdeserialized = FacultyMember(member_data["name"], member_data["member_id"])
                else:
                    memberdeserialized = Member(member_data["name"], member_data["member_id"])
                
                for isbn in member_data["borrowed_books"]:
                    memberdeserialized.borrowed_books.append(isbn)
                
                self.members[memberdeserialized.member_id] = memberdeserialized
