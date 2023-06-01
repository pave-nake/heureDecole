from datetime import datetime

now = datetime.now()

def write_highscore1(txt,score, name):
    with open(txt, "a") as file:
        file.write(f"{score} {name[0:8]} {now}\n")

def sort_highscores1(txt):
    scores = []
    with open(txt, "r") as file:
        for line in file:
            score, name,time1,time2 = line.strip().split(' ')
            scores.append((int(score), name,time1,time2))
    scores.sort(reverse=True)
    with open(txt, "w") as file:
        for score, name,time1,time2 in scores:
            file.write(f"{score} {name} {time1} {time2}\n")
