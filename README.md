# Library-management-system

## What does this project do?
This project uses object orientated programming to make a functional library. It uses class inheritance, json serialization and deserialization, as well as calling class methods from other files in an conditional statement, using the return value to determine the outcome. This project can create a library to store books in and register members with said library, this library can allow it's members to borrow books and return said books. The books also be listed based on no filter or the books available to borrow, as well the members currently borrowing books and what books they are borrowing. There is also a search feature that allows the user to search for a book in the library instance by title and author and returns matching results on both respectively. 

## What classes did I make?
### Book
This class is used to represent a single book and hold the attributes:
- title 
- author 
- isbn (13 digit)
- availability
This holds methods such as checking if the book is available for borrowing as well as displaying formatted titles with the author

### Member 
The Member class is suppoed to represent each individual member, has two sub classes that inherit the Member class:
- StudentMember
- Faculty Member 
The student member adopts the type 'Student' as well as only being able to borrow 3 books instead of the standard 5, while the factulty member has type 'Faculty' and can borrow 10 books at once. 
The attributes this class has is: 
- type (Standard)
- name 
- member_id
- borrowed_books (default = empty list)
This class also contains methods like borrowing and returning books but with the added functionality of appending the borrowed_books list with the isbn of each book borrowed for further functionality. 

### Library 
This class represents a single library, the books it holds and the members apart of it. It uses the attributes:
- books = dictionary where key is the isbn and value is the corresponding book object
- members = dictionary where key is the member_id and value is the corresponding member object
The library methods call many of the methods from the previous classes and use them to verify authenticity with the libraries current inventory of books and registered members. The inventory of books and list of members can be added to and changed through it's methods:
- register_member()
- add_book()
- remove_book()
Their are additonal methods as well allowing users to search the library for members and their currently borrowed books, as well as the total list of books the library owns.  

## How do I run it?

First donwload all the code, then in main.py their should be imported classes from the other files but if they aren't their then make sure you have the following at the top of the file: 
from book import Book
from member import Member, StudentMember, FactultyMember
from library import Library
import json

You can create a library using this example:
lib1 = Library()

Then to add a book to the library you can do the following: 
1. Add a book with the book class
    book1 = Book({title}, {author}, {isbn})
2. Then add it to the libraries collection
    lib1.add_book(book1)

Members can be registered using the following: 
1. Add a member using the member class
    Member1 = Member({name}, {id})
    (Remember that if you want to add specifically a student or faculty member use:
    - StudentMember 
    or 
    - FacultyMember 
    preceding the parenthesis with the name and id)
2. Then register the member to the library
    lib1.register_member(Member1)

With these two methods done in library, we can now borrow books using the following:
lib1.borrow_book(Member1.member_id, book1.isbn)

We can list a member's books with the method:
lib1.list_member_books(Member1.member_id)
(using no paramters will list all the books being borrowed by each registered member)

We can list all the books the library has available with: 
lib1.list_available_books()

Or we can just list all the books with: 
lib1.list_all_books()

Finally we can serealize and deserealize with the following methods:
**Seriealization**
lib1.serialization
**Deserialization**
(note for deserealization the json file must be name 'Library.json' to work)
lib1.deserialization


## What OOP concepts did I use?
The variety of concepts used in this project were: 

**Inheritance**
I used inheritance to make my code more streamlined with the sub classes StudentMember and FacultyMember inheriting the Member class, this allowed me to use the dunder init method as well as adding additional attributes like type changes and modifying the number of books that can be borrowed for each sub class.

**Classes and Objects**
I created 3 classes and 2 subclasses (Book, Member, StudentMember, FacultyMember, Library). Each class can have multiple objects, for example I created 11 different book objects when testing my code. 

**Method Overriding**
I call the default init method in both subclasses of Member with super().__init__() but I changed the attribute of the type to be different, this way the subclass would have the correct corresponding type. 

**Polymorphism**
The Member class and it's subclasses ((Faculty/Student)Member) all use the same methods but the borrow_book() method in particular actually changes in terms of functionality based on the object's max_books value determined by it's class/subclass.

**Encapsulation**
Instead of changing a book's attribute for it's availablity directly, I used encapsulation with the methods borrow() and return_book() to allow for not only a check of the value to make sure it's available but to also allow that to return a value for methods calling it from other places. 


## What was hard and what did I learn?
Today I learned how to use classes and objects effectively in a large scale environemt, this includes allowing methods to interact with other classes. Maintaining my code with effective documentation, providing changed in order of: Initialization of class methods, adding additional features, implementing file persistance and adding documentation. 

I also learned how to effectively test my code with each addition as well as making changes public through frequent but also valuable git commits. I will admit though as the project grew in size and I added more and more classes, it became harder to keep track of all the individual smaller peices that made up the bigger picture. Like for example when it came to serialization I felt like I really stuggled to turn all the objects in the borrowed_books list into just isbn's and back which is why I switched to isbn's permenantly instead as I thought it would integrate better with the methods in the library class that use isbn's as their paramters. 

## Code Statistics 
-- **Total line of code:** 469
-- **Classes:** 5 
-- **Methods:** 29
-- **Files:** 4 Python files