#NOTE: Possibly add the methods as class methods instead?

class Library:
    def __init__(self):
        books = {}
        members = {}
    
    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member