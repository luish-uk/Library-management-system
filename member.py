

class Member:
    max_books = 5
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        if self.max_books > (len(self.borrowed_books)):
            return self.borrowed_books.append(book)
        else:
            return 'You have reached your limit for borrowed books, please return a book to borrow this one'

    def return_book(self, book):
        return self.borrowed_books.remove(book)
    
    def get_borrowed_books(self):
        return self.borrowed_books
    
    def __str__(self):
        return 'Name: {}\nID: {}\nBorrowed: {}'.format(self.name, self.member_id, self.borrowed_books)
    
class StudentMember(Member):
    max_books = 3

class FacultyMember(Member):
    max_books = 10


sdt_1 = StudentMember('Luis Hernandez', 1)
fct_1 = FacultyMember('John Doe', 2)

print(sdt_1.borrow_book('Atomic Habits'))
print(sdt_1.borrow_book('Deep Work'))
print(sdt_1.borrow_book('Never finished'))
print(sdt_1.borrow_book('Can\'t hurt me'))


print(fct_1.borrow_book('Atomic Habits'))
print(fct_1.borrow_book('Deep Work'))
print(fct_1.borrow_book('Never finished'))
print(fct_1.borrow_book('Can\'t hurt me'))
print(fct_1.borrow_book('Atomic Habits'))
print(fct_1.borrow_book('Deep Work'))
print(fct_1.borrow_book('Never finished'))
print(fct_1.borrow_book('Can\'t hurt me'))
print(fct_1.borrow_book('Atomic Habits'))
print(fct_1.borrow_book('Deep Work'))
print(fct_1.borrow_book('Never finished'))
print(fct_1.borrow_book('Can\'t hurt me'))
