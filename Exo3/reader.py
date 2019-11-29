""" Exercices 3 """

class Reader():
    """book method"""
    def __init__(self):
        self.book = None 
        self.page = 0

        """method to impress the book"""
    def borrow_book(self, library, title):
        self.book=library.get_book(title)
        if self.book is None:
            raise Exception ("Le livre n'est pas disponible")
        else:
            self.page = 1
    
        """method to go to the page"""
    def go_to_page(self, page):
        self.page = page
       
        """method to go to the next page"""
    def next_page(self):
        return self.page +1
       

        """method to return to the previous page"""
    def previous_page(self):
        if page == 1:
            return
        return self.page -1
        

        """read method"""
    def read(self, book):
        return self.pages

        """method to read the book"""
    def read_book(self):
        self.pages = len(self.book.pages)