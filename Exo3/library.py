""" Exercices 3 """

class Library():
    
    """constructor class for books"""
    def __init__(self):
        self.books_list=list()

    """method to add books"""
    def add_book(self, book):
        self.books_list.append(book)

    """method to take the book"""
    def get_book(self, title):
        for book in self.books_list:
            if book.title==title:
                return book
        return None