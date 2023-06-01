# -*- coding: utf-8 *-*
#
# Exemple 2_28
# Exemple de Widget
#
from tkinter import *   # Import des modules de la bibliothèque tkinter

# Fonction couleur créée avant d'être appelée
def couleur():
    titre["bg"]="cyan"
    titre["fg"]="red"

def modif():
    texte = StringVar() 	# Associer une variable chaine
    texte = saisie.get()
    titre["text"]=texte


fenetre = Tk() 	# objet fenetre à partir de la classe Tk() fenetre principale
fenetre.minsize(100,100)
# titre = Objet de classe Label, argument fenetre, fenetre = objet parent de l'objet titre
titre = Label(fenetre, text="Bienvenue en ISN",fg='blue', bg="yellow")

bouton_titre=Button(fenetre, text="Titre",bd=5) 	# fenetre = objet parent, text = argument
bouton_fermer=Button(fenetre, text="Fermer", command=fenetre.destroy)
bouton_couleur=Button(fenetre, text="Couleur",fg="red",bg="cyan",bd=5,command=couleur)  # Fonction couleur associée
saisie=Entry(fenetre,width=50)

# Interface graphique n'existe pas, représentation interne des objets
# Méthode .pack() définit les paramètres géométriques au gestionnaire de position
titre.pack()
saisie.pack()
bouton_titre.pack()
bouton_couleur.pack(side=LEFT)
bouton_fermer.pack(side=RIGHT)

bouton_titre["command"] = modif # propriété command de la classe Button

# Représentation géométrique interne mais pas visible
# Methode mainloop tourne en boucle
# gestionnaire d'événement + affichage fenetre








fenetre.mainloop()
