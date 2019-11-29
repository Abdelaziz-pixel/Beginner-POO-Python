Exercice 3 :


Cet exercice est un peu plus long. Il va vous montrer comment la programmation orientée
objet nous permet de modéliser les processus physiques du monde qui nous entoure.
Dans cet exercice, vous allez modéliser une bibliothèque très simple et un lecteur qui vient
emprunter un livre et le lit. Pour vous aider, les fichiers vides des classes vous ont été
donnés ainsi qu’un fichier contenant une liste de livres. Vous trouverez également un
fichier main.py avec un script d’exécution du code pré-écrit. Votre objectif est de faire en
sorte que ce code soit fonctionnel sans modifications.
Votre programme sera composé des objets suivants :
- Le livre, il est composé d’un titre, du numéro de page par défaut sur lequel on se trouve
et d’une liste de pages. Par simplicité, dans le fichier books_list, vous verrez qu’il est
simplement écrit ‘page1’, ‘page2’ etc. Dans le cadre d’une vraie application ces chaînes de
caractères seraient beaucoup plus longues et contiendraient aussi la mise en forme et les
retour à la ligne. Attention le fichier books_list ne contient pas les objets livre, il contient les
données des livres à faire rentrer dans des objets, à vous de coder la classe Book en
conséquence.
- La bibliothèque, elle contient simplement la liste des objets livre, tout comme une
bibliothèque dans le monde réel n’est qu’un entrepôt pour livre. Elle peut rajouter des
livres à son catalogue et renvoyer l’objet livre correspondant sur la base d’un titre.
- Le lecteur, il ne contient que le livre qu’il a emprunté. Il peut réaliser plusieurs actions. Il
peut emprunter un livre, aller à une page spécifique du livre, aller à la page suivante, aller
à la précédente, lire une page c’est à dire afficher son contenu à l’écran et enfin lire
l’entièreté du livre.
