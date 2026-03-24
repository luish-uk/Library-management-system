

class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False
        
    def get_info(self):
        return self.__dict__
    

    def return_book(self):
        self.is_available = True
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
    

