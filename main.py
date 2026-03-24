from book import Book
from member import Member, StudentMember, FacultyMember
from library import Library

# Create library
lib = Library()

# Add some books
book1 = Book("Atomic Habits", "James Clear", 9780735211292)
book2 = Book("Deep Work", "Cal Newport", 9781455586691)
book3 = Book("Can't Hurt Me", "David Goggins", 9781544512280)

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

# Register members
student = StudentMember("Luis Hernandez", 1)
faculty = FacultyMember("John Doe", 2)

lib.register_member(student)
lib.register_member(faculty)

# Borrow books
lib.borrow_book(student.member_id, book1.isbn)
lib.borrow_book(faculty.member_id, book2.isbn)

# List member books
lib.list_member_books()

# Search
lib.search_books("Deep")

# Save library
lib.serialization()

# Demonstrate loading
lib2 = Library()
lib2.deserialization()
print("\n--- After loading from file ---")
lib2.list_all_books()