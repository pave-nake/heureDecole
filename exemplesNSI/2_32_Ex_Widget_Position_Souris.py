# -*- coding: utf-8 *-*
#
# Exemple 2_31
# Position de la souris
#

from tkinter import *

def Clic(event):
    """ Gestion de l'événement Clic gauche sur la zone graphique """
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    # on dessine un carré
    r = 10
    Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline='black',fill='red')

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title('Détection de la position de la souris')

# Création d'un widget Canvas
Canevas = Canvas(fenetre, width = 300, height =200, bg ='cyan')
# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la zone graphique provoquera l'appel de la fonction utilisateur Clic()
Canevas.bind('<Button-1>', Clic)
Canevas.pack(padx =5, pady =5)

bouton=Button(fenetre, text ='Quitter', command = fenetre.destroy)
bouton.pack(side=RIGHT,padx=5,pady=5)

fenetre.mainloop()