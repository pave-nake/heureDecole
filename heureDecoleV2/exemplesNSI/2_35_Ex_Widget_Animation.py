# -*- coding: utf-8 *-*

#
# Exemple 2_34
# Animation d'un widget
#

from tkinter import *

# fonction de déplacement
def Move():
    global X,Y
    if JEU == True:
        Y=Y+3
        Canevas.coords(proj,X,Y,X+TAILLE,Y+TAILLE)
        if Y < 180 :
        # mise à jour toutes les 50 ms
            fenetre.after(50,Move)
            print(Y)
        else :
            print(Y)

# fonction qui met le jeu en pause
def Pause():
    global JEU
    if JEU == True:
        JEU = False
    else :
        JEU = True
        Move()

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Animation")

# Constantes
JEU = True        # Si JEU == 0 pas de mouvement
LARG = 200        # Taille du canevas
HAUT = 200
TAILLE = 12    # Taille de la cible
X = LARG/2
Y = 10

# Création d'un widget Canvas
Canevas = Canvas(fenetre,width=LARG,height=HAUT,bg ='cyan')

# Projectile
proj = Canevas.create_oval(X,Y,X+TAILLE,Y+TAILLE,fill='red')

Canevas.pack(padx=10,pady=10,side=LEFT)
bouton_animer = Button(fenetre,bd=5,text = " Jouer ",bg='blue',command = Move)
bouton_pause = Button(fenetre,text = " Pause ",bg='green',command = Pause)
bouton_quitter = Button(fenetre,text = " Quitter ",bg='red' ,command = fenetre.destroy)

bouton_animer.pack(side=TOP,padx=10,pady=10)
bouton_pause.pack(side=TOP,padx=50,pady=50)
bouton_quitter.pack(side=BOTTOM,padx=10,pady=10)
fenetre.mainloop()