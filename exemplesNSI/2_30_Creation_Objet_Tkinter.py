# -*- coding: utf-8 *-*
#-----------------------------------------------------
# Cours 2_25 : Création objets TKinter
#-----------------------------------------------------
#
# On importe la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange
from PIL import Image, ImageTk

#-----------------------------------------------------
# Les fonctions
#-----------------------------------------------------
def Vaisseau():
    # On dessine le vaisseau une position aléatoire
    Xv = randrange(0,250)
    Yv = randrange(0,250)
    Canevas.coords(vaisseau,Xv,Yv)

def Carre():
    # On dessine un carré dans une position aléatoire
    Xc = randrange(0,250)
    Yc = randrange(0,250)
    Canevas.create_rectangle(Xc,Yc,Xc + TAILLE,Yc + TAILLE,fill="green")

def Disque():
    # On récupère la valeur de la variable couleur
    pass


#-----------------------------------------------------
# Les constantes
#-----------------------------------------------------
LARG=300       # Taille du canevas
HAUT=300
TAILLE = 10    # Taille des objets

#-----------------------------------------------------
# Les fenetres
#-----------------------------------------------------
# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Graphique")

label_1 = Label(fenetre,text = "Titre de mon jeu",fg = 'blue', bg = "yellow",font = "Arial 15 italic")
label_1.pack(padx = 5,pady = 5)

# Fenetre qui contient le choix des couleurs
frame_1 = Frame(fenetre,width = 350,height = 100,bg = "grey",bd = 4,relief = RAISED)
frame_1.pack(padx = 5,pady = 5)

# On créé une variable Tkinter associée à la couleur
# no_couleur.get() pour récupérer la valeur
no_couleur = IntVar ()
choix_1 = Radiobutton (frame_1,text = " Rouge ",variable = no_couleur,value = 1)
choix_1.grid(row = 0,column = 0,padx = 10,pady = 5)

# Fenetre Affichage de la couleur choisie
frame_2 = Frame(fenetre,width = 350,height = 100,bg = "grey",bd = 4,relief = RAISED)
frame_2.pack(padx = 5,pady = 5)
label_2 = Label(frame_2,text="Couleur choisie : ",fg = 'blue', bg = "yellow",font = "Arial 15 italic")
label_2.grid(row = 0,column = 0,padx = 10,pady = 5)

label_3 = Label(frame_2,text = "...",fg = 'blue', bg = "yellow",font = "Arial 15 italic")
label_3.grid(row = 0,column = 1,padx = 10,pady = 5)

# Le canevas
Canevas = Canvas(fenetre,width = LARG,height = HAUT,bg ='cyan')
Canevas.pack(padx = 5,pady = 5)

# On récupère l'image du vaisseau
image_vaisseau = ImageTk.PhotoImage(file ="2_30_Vaisseau.png")
vaisseau = Canevas.create_image(100,250,anchor = NW, image = image_vaisseau)

# Les boutons
bouton_vaisseau = Button(fenetre,text = " Vaisseau ",bg = 'yellow',command = Vaisseau)
bouton_carre = Button(fenetre,text = " Carrés ",bg = 'green',command = Carre)
bouton_quitter = Button(fenetre,text = " Quitter ",bg = 'red' ,command = fenetre.destroy)

bouton_vaisseau.pack(side = LEFT,padx = 10,pady = 10)
bouton_carre.pack(side = LEFT,padx = 10,pady = 10)
bouton_quitter.pack(side = RIGHT,padx = 10,pady = 10)

fenetre.mainloop()
