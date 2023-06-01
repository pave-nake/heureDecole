# -*- coding:Utf-8 -*-

# ***********************************
# Cours 2_31 : Vaisseau et Comete
# ***********************************

# On importe la bibliothèque graphique Tkinter
from tkinter import *
from PIL import Image, ImageTk
import random

# fonction de déplacement
def Clavier(event):
    global Xv,Yv,JEU
    touche = event.keysym
    if JEU == True:
        # déplacement vers la droite
        if touche == 'Right':
            Xv = Xv + DEP_V
        # déplacement vers la gauche
        if touche == 'Left':
            Xv = Xv - DEP_V
        # on dessine le vaisseau à sa nouvelle position
        Canevas.coords(vaisseau,Xv,Yv)

def Jouer():
    global Xc,Yc
    nb=nb_comete.get()
    for i in range(nb):
        Xc[i] = random.randrange(LARG)
        Yc[i] = 0
        ntag = "comete_"+str(i)
        Comete[i] = Canevas.create_oval(Xc[i],10,Xc[i]+TAILLE_C*2,10+TAILLE_C*2,fill='red',tag=ntag)
    Move_C()

def Move_C():
    if JEU == True:
        for i in Comete.keys():
            Yc[i]= Yc[i]+DEP_C
            Canevas.coords(Comete[i],Xc[i],Yc[i],Xc[i]+TAILLE_C*2,Yc[i]+TAILLE_C*2)
            if Yc[i] > 300:
                Yc[i] = 0
        # mise à jour toutes les 50 ms
        fenetre.after(50,Move_C)

def Detruire():
# Supprime une comete
    global no_detruit
    ntag ="comete_"+str(no_detruit)
    Canevas.delete(ntag)
    no_detruit = no_detruit + 1

# Constantes
JEU = True        # Si JEU == 0 pas de mouvement
LARG=300          # Taille du canevas
HAUT=300
DEP_V = 5         # Increment de déplacement du vaisseau
DEP_C = 3         # Increment de déplacement des comètes
DEP_B = 10        # Increment de déplacement de la balle
TAILLE_C = 12     # Taille de la comete
TAILLE_P = 3      # Taille du projectile
Xv = 100          # Position initiale du vaisseau
Yv = 250
Xc = [0] * 5      # Inialisation position des comètes
Yc = [0] * 5
no_detruit = 0

# On créé un dictionnaire contenant les cometes
Comete={}

# On crée la fenêtre principale
fenetre = Tk()
fenetre.title("Jeu des comètes")

label_1 = Label(fenetre,text = "Nombre de comètes",fg = 'blue', bg = "yellow",font = "Arial 15 italic")
label_1.pack(padx = 5,pady = 5)

# Fenetre qui contient le nombre de comètes
frame_1 = Frame(fenetre,width = 350,height = 100,bg = "grey",bd = 4,relief = RAISED)
frame_1.pack(padx = 5,pady = 5)

nb_comete = IntVar ()
choix_1 = Radiobutton (frame_1,text = " 1 ",variable = nb_comete,value = 1)
choix_2 = Radiobutton (frame_1,text = " 2 ",variable = nb_comete,value = 2)
choix_3 = Radiobutton (frame_1,text = " 3 ",variable = nb_comete,value = 3)
choix_4 = Radiobutton (frame_1,text = " 4 ",variable = nb_comete,value = 4)
choix_1.grid(row = 0,column = 0,padx = 10,pady = 5)
choix_2.grid(row = 0,column = 1,padx=10,pady = 5)
choix_3.grid(row = 0,column = 2,padx=10,pady = 5)
choix_4.grid(row = 0,column = 3,padx=10,pady = 5)

# Le canevas
Canevas = Canvas(fenetre,width = LARG,height = HAUT,bg ='cyan')
Canevas.pack(padx = 5,pady=5)

# On récupère l'image du vaisseau
image_vaisseau = ImageTk.PhotoImage(file="2_31_Vaisseau.png")
vaisseau = Canevas.create_image(100,250,anchor = NW, image = image_vaisseau)

# La méthode bind() permet de lier un événement avec une fonction
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)

# Les boutons
bouton_jouer = Button(fenetre,text = " Jouer ",bg = 'blue',command = Jouer)
bouton_detruire = Button(fenetre,text = " Détruire ",bg = 'green',command = Detruire)
bouton_quitter = Button(fenetre,text = " Quitter ",bg = 'red' ,command = fenetre.destroy)

bouton_jouer.pack(side=LEFT,padx = 10,pady = 10)
bouton_detruire.pack(side = LEFT,padx = 50,pady = 10)
bouton_quitter.pack(side = RIGHT,padx = 10,pady = 10)

fenetre.mainloop()
