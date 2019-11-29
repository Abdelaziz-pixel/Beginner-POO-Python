""" Exercices 1"""

"""the constructor contains two attributes, a name and a department"""
class City: 
    def __init__(self, nom, département): 
        self.mon_nom = nom 
        self.mon_département = département 

    def show_localisation(self): 
        """method to display given attributes which is the name and the department"""
        print("La ville {} se trouve dans le département {} ".format(self.mon_nom, self.mon_département))

    def change_localisation(self,nom,département): 
        """method to change given attributes which is the name and the department"""
        self.mon_nom = nom 
        self.mon_département = département 


