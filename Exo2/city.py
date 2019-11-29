""" Exercices 2 """
"""importing the cities file"""
from cities import * 

class City:
    """constructor class containing several elements"""
    def __init__(self, i):
        self.name = None  
        self.departement = None 
        self.country = None
        self.population = None 
        self.mayor = None 
        self.capital = None
        self.hydrate(i)

    """method to hydrate the attributes"""
    def hydrate(self, i):
        for key, value in i.items():
            if hasattr(self, key):
                setattr(self, key, value)

    """method to display the elements of the cities file"""
    def show_information(self):
        text = "------------------\n \
        name: {}\n \
        departement: {}\n \
        country: {}\n \
        population: {}\n \
        mayor: {}\n \
        capital: {}\n"
        print(text.format(self.name, self.departement, self.country, self.population, self.mayor, self.capital))

