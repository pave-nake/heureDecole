# classe calme->hold button->gain points->door open->teacher notice->game over
# 						->stop click->teacher doesnt notice->continue
# 						->student enter->continue
# 		->stop hold->pause gain points
# ->speeds up door opening

#TODO
#-playtest
#(do ui for the other games)
################################################################

import tkinter as tk
from tkinter import ttk
from random import randint as ri
from datetime import datetime


#######################################################
# travaille numero 1:
# la fonction gameover() termine le jeux
# 
#  def fonction():
    # fen.after(milisecondes,fonction)
#
# faire fonction life_ennuibar() qui ajoute un numbre a ennui_value chaque ... secondes
#######################################################


#######################################################
# travaille numero 2:
# ecrire le highscore avec une fonction ecrire_high() qui met la variable {name} et {score} dans un txt file
# ecrire une deuxieme fonct affiche_high() qui return les 3 scores les plus haut et les noms depuis le txt file
# utilise internet pour voir comment manipuler txt file (exemple:https://www.w3schools.com/python/python_file_open.asp)
#######################################################

fen = tk.Tk()
fen.title("jeu- Equipe 5 PROTOTYPE HEURE D ECOLE vers1.00")
fen.geometry("960x540")
fen.configure(bg="grey")
fen.resizable(False, False)

canvas = tk.Canvas(fen, width=960, height=540,bg='grey')
canvas.pack()

style = ttk.Style()
style.theme_use()

################################################################

typeofstudents=['stick','vadim','chamber']
is_started=False
door_open=False
held_down = False
score=0
multiplier=1
name=None
dooreventscompleted=0
ennui_value=0
recursive=True
scoredelay=500
bonuscombo=0

################################################################

imagestart =tk.PhotoImage(file="heureDecoleV2/resources/CLASSROOMclosed.png") 
classclosednormal=tk.PhotoImage(file="heureDecoleV2/resources/CLASSROOMnormalclosed.png")
classopennormal=tk.PhotoImage(file="heureDecoleV2/resources/CLASSROOMnormalopen.png") 
classclosedchaos=tk.PhotoImage(file="heureDecoleV2/resources/CLASSROOMchaosclosed.png") 
classopenchaos=tk.PhotoImage(file="heureDecoleV2/resources/CLASSROOMchaosopen.png") 
student1=tk.PhotoImage(file="heureDecoleV2/resources/stick.png") 
student2=tk.PhotoImage(file="heureDecoleV2/resources/vadim.png")
student3=tk.PhotoImage(file="heureDecoleV2/resources/chamber.png") 
teacherangry=tk.PhotoImage(file="heureDecoleV2/resources/teacherangry.png")
teachercalm=tk.PhotoImage(file="heureDecoleV2/resources/teachercalm.png")
gameover_image=tk.PhotoImage(file="heureDecoleV2/resources/game_over.png")
logo=tk.PhotoImage(file="heureDecoleV2/resources/logo.png")

################################################################

gameversion=canvas.create_text(200, 520, text='game ver. 1.01', font=("Arial", 18), fill="white",)

class_image_item = canvas.create_image(480,270, image=imagestart,)
teacher_image_item=canvas.create_image(720,235, image='',)
student_image_item=canvas.create_image(720,235, image='',)
gameover_image_item=canvas.create_image(480,310, image='',)
highscoretop3=canvas.create_text(120, 160, text='', font=("Arial", 18), fill="white",width=250)
displayedscore=canvas.create_text(360,155,text='', font=("Arial", 23), fill="white",)
logo_image = canvas.create_image(500,135, image=logo,)

################################################################

##arsenii

txt="heureDecoleV2/resources\highscores.txt"


def write_highscore(txt,score,name):
    with open(txt, "a") as file:
        file.write(f"{score} {name[0:8]}\n")


def sort_highscores(txt):
    scores = []
    with open(txt, "r") as file:
        for line in file:
            score, name = line.strip().split(' ')
            scores.append((int(score), name))
    scores.sort(reverse=True)
    with open(txt, "w") as file:
        for score, name, in scores:
            file.write(f"{score} {name}\n")



def chrono():
    global score
    if is_started==True:
        score=score+1
        fen.after(200,chrono)
        display_score()



################################################################
#controls

#chaos button
use_button = tk.Button(fen, text="chaos!",bg='light grey',width=10, height=2,font=10)
use_button.place(x=0, y=500)

def button_press(event):
    global held_down
    held_down = True
    if door_open and is_started:canvas.itemconfigure(class_image_item, image=classopenchaos)
    elif is_started and not door_open:canvas.itemconfigure(class_image_item, image=classclosedchaos)

def button_release(event):
    global held_down
    held_down = False
    if door_open and is_started:canvas.itemconfigure(class_image_item, image=classopennormal)
    elif is_started and not door_open:canvas.itemconfigure(class_image_item, image=classclosednormal)


def enable_controls():
    use_button.bind("<ButtonPress-1>", button_press)
    use_button.bind("<ButtonRelease-1>", button_release)
    fen.bind("<KeyPress>", button_press)
    fen.bind("<KeyRelease>", button_release)
enable_controls()

def remove_controls():
    use_button.place_forget()
    fen.unbind("<KeyPress>")
    fen.unbind("<KeyRelease>")

################################################################
def highscorescreen():
    with open("heureDecoleV2/resources/highscores.txt", "r") as file:
        scores = file.readlines()
    top3=scores[0:3]
    hs=f''
    for elem in top3:
        scoretop,nametop=elem.split(' ')
        if "\n" in nametop:
            nametop=nametop[:-1] 
        hs=hs+str(f'{nametop[:8]}: {scoretop}'+"\n")
    canvas.itemconfigure(highscoretop3, text='top 3 ranking:'+"\n"+hs)
highscorescreen()

highscorescreen()
def removehighscorescreen():
    canvas.itemconfigure(highscoretop3, text='')

def create_retry_button():
    global retry_button
    retry_buttonpress = tk.Button(canvas, text="retry",bg='red',width=10, height=2,font=10,command=retry)
    retry_button=canvas.create_window(480, 400, window=retry_buttonpress,tags="retrybutton")
def retryaction():
    global score,retry_button
    score=0
    removevisitor()
    removehighscorescreen()
    canvas.itemconfigure(displayedscore,text='')
    canvas.itemconfigure(gameover_image_item, image='')
    canvas.itemconfigure(displayedscore, text='')
    highscorescreen()
    canvas.itemconfigure(class_image_item, image=imagestart)
    canvas.itemconfigure(logo_image,image=logo)
    create_start_button()
    create_quit_button()
    create_name_entry()
def retry():
    canvas.delete("retrybutton")
    retryaction()

def remove_quitgame():
    canvas.delete(quit_button)
def quitgame():
    exit()
def create_quit_button():
    global quit_button
    quit_buttonpress = tk.Button(canvas, text="QUIT",bg='red',width=10, height=2,font=10,command=quitgame)
    quit_button=canvas.create_window(900, 490, window=quit_buttonpress)
create_quit_button()

def on_start_click():
    canvas.itemconfigure(gameversion,text='')
    canvas.delete(start_button)
    started()
def create_start_button():
    global start_button
    start_button = tk.Button(fen, text="Start", command=on_start_click,bg='light green',width=10, height=2,font=10)
    start_button=canvas.create_window(500,325,window=start_button)
create_start_button()

def remove_name_entry():
    global inputed
    canvas.delete(inputed)
def get_name():
    global name
    name=name_entry.get()
    return name
def create_name_entry():
    global inputed,name_entry
    name_entry = tk.Entry(canvas,width=15)
    inputed=canvas.create_window(495, 450, window=name_entry,)
    name_entry.insert(tk.END, "name=")
create_name_entry()
def remove_name_entry():
    global inputed
    canvas.delete(inputed)

def create_progressbar():
    global progressbar,bar_ennui,text_bar_ennui,ennui_value
    offset=40
    progressbar = ttk.Progressbar(canvas, orient=tk.HORIZONTAL, length=500, mode='determinate',)
    bar_ennui=canvas.create_window(550-offset, 15, window=progressbar)
    text_bar_ennui=canvas.create_text(265-offset, 13, text='ennui', font=("Arial", 15), fill="black",)
    progressbar['value'] = ennui_value
def remove_progressbar():
    global progressbar,bar_ennui,text_bar_ennui
    canvas.delete(bar_ennui)
    canvas.delete(text_bar_ennui)

################################################################
def gameover():
    global is_started,held_down,recursive
    recursive=False
    remove_progressbar()
    remove_controls()
    held_down=False
    is_started=False
    name_entry.unbind("<Key>")
    canvas.itemconfigure(gameover_image_item, image=gameover_image)
    write_highscore(txt,score,name)
    sort_highscores(txt)
    highscorescreen()
    create_retry_button()
    create_quit_button()
    fen.after(5000,gameover2)
def gameover2():
    removevisitor()

def started():
    global is_started,name,name_entry,ennui_value,recursive
    recursive=True
    create_progressbar()
    remove_name_entry()
    canvas.focus_set()
    enable_controls()
    ennui_value=0
    is_started=True
    namea=get_name()
    if namea=="name=":name='guest'
    else:name=namea[5:]
    canvas.itemconfigure(class_image_item, image=classclosednormal)
    canvas.itemconfigure(logo_image,image='')
    removehighscorescreen()
    chrono()
    fen.after(ri(3000,(20000-dooreventscompleted)), door_events)
    canvas.focus_set()
    name_entry.unbind("<Key>")
    name_entry.place_forget()
    life_ennuibar()
    remove_quitgame()

def teacher():
    if held_down:
        canvas.coords(teacher_image_item,712,235)
        canvas.itemconfigure(teacher_image_item, image=teacherangry)
    else:
        canvas.coords(teacher_image_item,720,235)
        canvas.itemconfigure(teacher_image_item, image=teachercalm)

def removevisitor():
    canvas.itemconfigure(teacher_image_item, image='')
    canvas.itemconfigure(student_image_item, image='')


def closedoor():
    global door_open
    door_open=False
    if held_down:canvas.itemconfigure(class_image_item, image=classclosedchaos)
    else:canvas.itemconfigure(class_image_item, image=classclosednormal)

def opendoor():
    global door_open
    door_open=True
    if held_down:canvas.itemconfigure(class_image_item, image=classopenchaos)
    else:canvas.itemconfigure(class_image_item, image=classopennormal)

def display_score():
    global score
    canvas.itemconfigure(displayedscore,text="score:"+str(round(score,2)))

################################################################

def life_ennuibar():
    global ennui_value,recursive
    if recursive:fen.after(200, life_ennuibar)
    if ennui_value>99:
        ennui_value=0
        gameover()
    if held_down and ennui_value>=0:ennui_value-=2
    else:ennui_value+=2
    progressbar['value'] = ennui_value

################################################################

def door_events():
    global dooreventscompleted,door_open,held_down,typeofstudents,event,recursive
    dooreventscompleted+=1000
    # if recursive:fen.after(ri(8000-dooreventscompleted,20000-dooreventscompleted), door_events)
    if recursive:fen.after(ri(4000-dooreventscompleted,16000-dooreventscompleted), door_events)

    listeposib=['teacher','teacher','teacher','student']
    event=listeposib[ri(0,len(listeposib)-1)]
    if recursive:opendoor()
    fen.after(int(4000-(dooreventscompleted*0.5)), continue_doorevents1)
def continue_doorevents1():
    global event,recursive
    if event=='student' and recursive:continue_doorevent_student1()
    elif event=='teacher' and recursive: continue_doorevent_teacher()

def continue_doorevent_student1():
    global typeofstudents,scoredelay,bonuscombo
    studentvariation=ri(0,2)
    if typeofstudents[studentvariation]=='stick':newimage=student1
    elif typeofstudents[studentvariation]=='vadim':newimage=student2
    elif typeofstudents[studentvariation]=='chamber':newimage=student3
    canvas.itemconfigure(student_image_item, image=newimage)
    if scoredelay>200:
        scoredelay-=50
        bonuscombo+=1
    fen.after(2000,continue_doorevent_closingdoor1)

def continue_doorevent_teacher():
    global held_down,recursive
    if held_down==False:
        teacher()
        if recursive:fen.after(ri(750,2000),continue_doorevent_closingdoor1)
    else:
        teacher()
        if recursive:fen.after(1500,caught)

def caught():
    global is_started
    is_started=False
    remove_progressbar()
    remove_controls()
    fen.after(2000,caught2)
def caught2():
    gameover()

def continue_doorevent_closingdoor1():
    global held_down,event;recursive
    if event=='teacher' and held_down==True:
        teacher()
        continue_doorevent_teacher()
        removevisitor()
        if recursive and event=='teacher':teacher()
        if recursive and event=='teacher':caught()
    else:    
        removevisitor()
        if recursive:fen.after(750,continue_doorevent_closingdoor2)

def continue_doorevent_closingdoor2():closedoor()

################################################################




################################################################

fen.mainloop()
