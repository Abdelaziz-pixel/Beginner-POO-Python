""" Exercices 3 """

class Book():
    
    def __init__(self,**parametre):
        self.title=parametre["title"]
        self.pages=parametre["pages"]

    def __str__(self):
        return "Title: {0}, Pages:\n {1}".format(self.title,self.pages)



        