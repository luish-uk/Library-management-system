
"""
This class stores information about a book and is used to check a book's attributes with each instance being an individual book
"""
class Book:
    """
    Initilizes book instance with a title, author and isbn 13 digit for identification, as well as setting the book to be automatially available.
    """
    def __init__(self, title, author, isbn):
        
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.is_available = True


    """
    Checks if book instance is marked as available for borrowing, then sets the availablity to false if it's availble and returns True to indicate the book is available to borrow.
    """
    def borrow(self):
        
        if self.is_available:
            self.is_available = False
            return True
        
        else:
            return False
        


    def get_info(self):
        return self.__dict__
    

    """
    Sets book to availble once returned
    """
    def return_book(self):
        self.is_available = True
    

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
    

    """
    Serializes the book object into a dictionary type with all it's attributes
    """
    def serialization(self):
        return self.__dict__

