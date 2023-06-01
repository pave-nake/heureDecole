from tkinter import*
from time import datetime
s=1
game=True


def chrono():
    global s
    if game==True:
        fenetre.after(1000,chrono)
        score["text"]=str(s)
        print(s)
        s=s+1
####detaim#####
fenetre = Tk()
fenetre.title("score")
score=Label(fenetre,text="0",fg="black",bg="white")
score_board=Label(fenetre,text='',fg="black",bg="white")
button=Button(fenetre,text="start",command=chrono)
button.pack()
score.pack()

now = datetime.now()
def write_highscore(scorebaord,score, name):
    with open(scorebaord, "a") as file:
        file.write(f"{score} {name[0:8]} {now}\n")

def sort_highscores(txt):
    scores = []
    with open(scorebaord, "r") as file:
        for line in file:
            score, name,time1,time2 = line.strip().split(' ')
            scores.append((int(score), name,time1,time2))
    scores.sort(reverse=True)
    with open(scorebaord, "w") as file:
        for score, name,time1,time2 in scores:
            file.write(f"{score} {name} {time1} {time2}\n")

score_board.pack()
fenetre.mainloop()