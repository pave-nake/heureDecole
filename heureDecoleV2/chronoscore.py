from tkinter import*
from datetime import datetime
s=1
game=True



####detaim#####
fenetre = Tk()
fenetre.title("score")
score=Label(fenetre,text="0",fg="black",bg="white")
score_board=Label(fenetre,text='',fg="black",bg="white")
button=Button(fenetre,text="start",command=chrono)
button.pack()
score.pack()



score_board.pack()
fenetre.mainloop()