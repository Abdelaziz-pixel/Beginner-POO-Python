""" Exercices 1"""

from city import *

nom = City("Paris",75)
nom.show_localisation()

nom = City("Calais",62)
nom.show_localisation()

nom = City("Marseille",13)
nom.show_localisation()

nom = City("Bordeaux",33)
nom.show_localisation()

nom = City("Roubaix",59)
nom.show_localisation()

nom.change_localisation("Roubaix",59100)
nom.show_localisation()
