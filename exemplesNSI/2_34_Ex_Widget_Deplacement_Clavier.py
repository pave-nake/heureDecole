# -*- coding: utf-8 *-*
#
# Exemple 2_33
# Déplacement au clavier
#

from tkinter import *

# fonction de déplacement

def Clavier(event):
    global X,Y
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'Up':
        Y = Y - DEP
    # déplacement vers le bas
    if touche == 'Down':
        Y = Y + DEP
    # déplacement vers la droite
    if touche == 'Right':
        X = X + DEP
    # déplacement vers la gauche
    if touche == 'Left':
        X = X - DEP
    # on dessine le pion à sa nouvelle position
    Canevas.coords(rond,X , Y , X + 20, Y + 20)

def Raz():
    Canevas.coords(rond,0,0,TAILLE*2,TAILLE*2)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Déplacement clavier")

# Création d'un widget Canvas
DEP = 5
TAILLE = 10
X = 0
Y = 0
Canevas = Canvas(fenetre,width=300,height=200,bg ='cyan')
# Création d'un objet graphique
rond = Canevas.create_oval(0,0,TAILLE*2,TAILLE*2,fill='red')

# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)

Canevas.pack(padx=10,pady=10,side=LEFT)
Button(fenetre,text=' Quitter' ,command=fenetre.destroy).pack(side=BOTTOM)
Button(fenetre,text=' RAZ' ,command=Raz).pack()

fenetre.mainloop()