import json
import csv
import random
from datetime import datetime as dt
try:
    with open("data.json", "r") as r:
        jdict= json.load(r)
except:
    print("File not found.")
    exit()
op= True
responses= ("a", "b", "c", "d")

def round():
    used_ques= []
    username= input("Type username\n >> ").capitalize()
    round_points= 0
    corrects= 5
    counter= 0
    while counter < 5:
        question= random.randint(0, 99)
        if question in used_ques:
            continue
        else:
            used_ques.append(question)
        for k, v in jdict[question].items():
            if k== "respuesta_correcta":
                correct_ans= v
            elif k== "categoria" or k== "id":
                continue
            elif k== "opciones":
                for k2, v2 in v.items():
                    print(f"{k2}) {v2}")
            else:
                print("-", v)
        answer= ""
        while answer not in responses:
            answer= input("Type answer\n >> ").lower()
            if answer not in responses:
                print("Invalid answer! Type it again")
        if answer== correct_ans.lower():
            round_points+= 20
            print(f"Correct!\nCurrent points -> {round_points}\n")
        else:
            print("Incorrect answer :(\n")
            corrects-= 1
        counter+= 1
    print(f"Round finished 8)\n Correct answers -> {corrects}\n Total points -> {round_points}/100")
    match_date= dt.now().strftime("%Y-%m-%d at %H:%M")
    user= [username, round_points, match_date]
    return user

def add_to_csv(user):
    with open("ranking.csv", mode="a") as f:
        writer= csv.writer(f)
        writer.writerow(user)

def see_leaderboard():
    try:
        with open("ranking.csv", mode= "r", newline= "") as f:
            reader= csv.reader(f)
            data= list(reader)
            data.sort(key=lambda x: int(x[1]), reverse=True)
            print("Leaderboad")
            for row in data:
                print(f"usernaname -> {row[0]}\n score -> {row[1]}\n date -> {row[2]}\n")
    except:
        print("There's no register for any match.")
        exit()

while op!= 3:
    try:
        op= int(input("Random topics trivia\n 1) Play\n 2) Leaderboard\n 3) Exit\n >> "))
        if op== 1:
            user= round()
            add_to_csv(user)
        elif op== 2:
            see_leaderboard()
        elif op== 3:
            print("Bye")
        else:
            raise ValueError
    except:
        print("Invalid option!")
