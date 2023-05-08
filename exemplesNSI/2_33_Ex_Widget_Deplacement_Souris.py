# -*- coding: utf-8 *-*
#
# Exemple 2_32
# Déplacement de la souris
#

from tkinter import *

def Move(event):
    """ Déplacement avec bouton de gauche """
    X = event.x
    Y = event.y
    Canevas.coords(rond,X-TAILLE,Y-TAILLE,X+TAILLE,Y+TAILLE)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Déplacement souris")

# Création d'un widget Canvas
TAILLE = 10
Canevas = Canvas(fenetre,width=300,height=200,bg ='cyan')
# Création d'un objet graphique
rond = Canevas.create_oval(0,0,TAILLE*2,TAILLE*2,fill='red')

# La méthode bind() permet de lier un événement avec une fonction
Canevas.bind('<B1-Motion>',Move) # événement bouton gauche enfoncé (hold down)

Canevas.focus_set()
Canevas.pack(padx=10,pady=10)

fenetre.mainloop()