#NOTE: Possibly add the methods as class methods instead?

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
