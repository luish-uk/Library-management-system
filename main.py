from book import Book
from member import Member, StudentMember, FacultyMember
from library import Library



book1 = Book("Atomic Habits", "James Clear", 9780735211292)
book2 = Book("Never Finished", "David Goggins", 9781544536828)
book3 = Book("Can't hurt me", "David Goggins", 9781544512280)
book4 = Book("Deep work", "Cal Newport", 9781455586691)
book5 = Book("Steve Jobs", "Walter Issacson", 9781982176860)
book6 = Book("Elon Musk", "Walter Issacson", 9781398527539)
book7 = Book("Fermats last theorum", "Simon Singh", 9781841157917)
book8 = Book("The Psychology of Money", "Morgan Housel", 9780857197689)
book9 = Book("Harry Potter and the Philosophers stone", "J.K. Rowling", 9780747532743)
book10 = Book("Kidnapped", "Robert Louis Stevenson", 9781764143035)
book11 = Book("Wonder", "R.J. Palacio", 9780375869020)


sdt_1 = StudentMember('Luis Hernandez', 1)
fct_1 = FacultyMember('John Doe', 2)



lib1 = Library()

book1.serialization()
lib1.add_book(book1)
lib1.add_book(book2)
lib1.add_book(book3)
lib1.register_member(sdt_1)
lib1.register_member(fct_1)
lib1.borrow_book(fct_1.member_id, book3.isbn)
lib1.borrow_book(sdt_1.member_id, book1.isbn)
lib1.borrow_book(sdt_1.member_id, book2.isbn)
print(sdt_1.serialization())
lib1.list_member_books(sdt_1.member_id)
lib1.serialization()
lib2 = Library()
lib2.deserialization()
lib2.list_all_books()
lib2.list_member_books()
lib2.__str__()