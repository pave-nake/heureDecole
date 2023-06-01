from tkinter import *


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
    
def life_ennuibar():
    global ennui_value,recursive
    if recursive:fen.after(200, life_ennuibar)
    if ennui_value>99:
        ennui_value=0
        gameover()
    if held_down and ennui_value>=0:ennui_value-=2
    else:ennui_value+=2
    progressbar['value'] = ennui_value

