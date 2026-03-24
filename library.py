from book import Book
from member import Member, StudentMember, FacultyMember
import json
#NOTE: List books that are overdue method, and a calculate late fees method 

"""
This library class initlizes a new library with an empty dictionary holding all the books it stores (in house and being borrowed) as well as all the registered members at the library including faculty
"""
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    """
    This method takes a book instance from the book class and if the book is not already in the books dictionary (stores all of the library instance books) with the key being the isbn attribute from the book parameter, it will therefore be added to the libraries collection, else it will return an error message
    """
    def add_book(self, book):
        if (book.isbn) not in self.books:
            self.books[book.isbn] = book
        else:
            return 'Error, this book has already been added'
    

    """
    Removes a book from the library via it's stored isbn attribute compared to the isbn attribute in the parameter. If the isbn passed in exists in the libraries collection of books (the books dictionary) then it will be removed, else it returns an error message.
    """
    def remove_book(self, isbn):
        if (isbn) in self.books:
            del self.books[isbn]
        else: 
            return 'Error, this book doesn\'t exist'
        
    
    """
    This method registers a member with the member method and compares the passed in object with the members dictionary holding all current members in the library, if they aren't in the dictionary via their member_id, they are added to the dictionary and the passed in object is the value, with the key being the member's id. If they already are registered then an error message is returned.
    """
    def register_member(self, member):
        if (member.member_id) not in self.members:
            self.members[member.member_id] = member
        else:
            return 'Error, this member already exists'


    """
    Returns a book object through the passed in isbn of the book
    """
    def get_book(self, isbn):
        return self.books[isbn]
    

    """
    Returns a member object through the passed in member_id
    """
    def get_member(self, member_id):
        return self.members[member_id]
    

    """
    This method:
    - Stores the member object retrieved through the members dictionary with the member_id key as borrower
    - Stores the book object retrieved through the book dictionary with the isbn key as book
    - Then using the member.borrow_book() method from the member class it:
    - - Checks the members not over the borrow limit
    - - Checks the book is available 
    - - Once both are true the member.borrow_book() returns true, else false
    - If it returns true then a conformation is printed, else then an error is printed instead 
    """
    def borrow_book(self, member_id, isbn):
        borrower = self.members[member_id] #Stores member object 
        book = self.books[isbn] #Stores book object
        if borrower.borrow_book(book) == True: 
            print("Success book as been borrowed - Library")
        else:
            print("Error book could not be borrowed - Library")


    """
    This method:
    - Uses a similar structure to borrowing a book, with the paramaters as keys to retrieve and store values to the variables book and returner
    - if the isbn is in the returner's (member instance) borrowed books then we can confirm the returner held the book, this then:
    - - calls the return book function from the book class which sets the book object attribute for available to True
    - - calls the return book from the member class which removes the book from their list of borrowed books 
    - conformation is printed
    - if the book wasn't in the returner's list of borrowed books and error is printed
    """
    def return_book(self, member_id, isbn):
        book = self.books[isbn] 
        returner = self.members[member_id]
        if isbn in returner.borrowed_books:
            book.return_book()
            returner.return_book(book)
            print("Success, book has been returned!")
        else:
            print("This member is not borrowing this book")


    """
    This method searches books with a passed in query:
    - stores the length of the query and the results found 
    - searches each book in the library by author and title, if the first characters of the same length as the query match (upper is added to allow for case-insensitive results) then the author/title is printed as well setting results_found to true
    - if not results were found a subsequent error is printed. 
    """
    def search_books(self, query): 
        print(f"\nSearch Results for '{query}':")
        results_found = False #Any results?
        length = len(query) #length of query 
        for item in self.books:
            result = self.books[item] #grabs book objects
            title = result.title 
            author = result.author
            if query.upper() == title[:length].upper(): #does query match the first characters (=length) of the books (title/author)
                print(result.__str__())
                results_found = True
            if query.upper() == author[:length].upper():
                print(result.__str__())
                results_found = True
        if results_found == False:
            print("Unable to find results from query")


    """
    Loops through all the books in the library and prints the fomatted string for them from the books class
    """
    def list_all_books(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())
    

    """
    list of available books is similar to list_all_books method but it checks the books availablity through the book class attribute
    """
    def list_available_books(self):
        print("\nAvailable Books:")
        for item in self.books:
            item = self.books[item]
            if item.is_available:
                print(item.__str__())


    """
    This method checks to see if a members id was passed in,
    if it there wasn't (default):
    - loops through reigstered members and prints their books from the method get_borrowed_books from the Member class, for each of the items in that list it prints book object retrived from using the isbn on the book collection dictionary as a key, printing the book object will default to the dunder str method in the book class
    if it was: 
    - it only calls the member's borrowed books method from the member class specified in this methods parameter and subsequently prints the dunder string method for each book using the list of borrowed book's isbn on the library's dictionary collection of books
    """
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

    """
    This method simply prints all the members and books currently logged in the libraries dictionaries, via for loops that iterate through each value pair and print the corresponding dunder string for that object
    """
    def __str__(self):
        print("\nBooks:")
        for item in self.books:
            print(self.books[item].__str__())

        print("\nMembers:")
        for person in self.members:
            print(self.members[person].__str__())


    """
    This method creates a new json file and calls both serilization methods from the member and book classes, then appends this to a list holding all corresponding members/books, it does this by iterating through each item in the dictionary types holding all the libraries members/books.
    """
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


    """
    This method deserilizes the file named 'Library.json' (it must be named this for it to work). It then resets the dictionaries holding all the data for the libraries books and members and subsequently fills them in through for each loops that use the data in the json objects to run the init methods on. 

    For the book class:
    - Book init is ran for each book
    - The book is assigned it's value for availablity since the default is True when calling the init method for every book instance
    - the book is added to the libraries book dictionary with the object as it's value and isbn as it's key

    For the member class:
    - It checks each type of member and then runs the appropriate class or sub class
    - The it runs another for each loop inside with each isbn being appended to the borrowed books list since it's empty for a new class instance by default 
    - Finally it adds the member to the library though the libraries dictionary of members with the member object being the value and the member_id being the key
    """
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
