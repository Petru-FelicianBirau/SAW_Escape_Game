from tutorial import tutorial
from intro import intro
from playsound import playsound
import Material as mat
import Variables as var
import time
import os
from colorama import Fore, Back, Style
import zimmer0_lib as z0
import zimmer1_lib as z1
import zimmer2_lib as z2

def interaktion13():
    az0=input("\nMit der Tür interagieren? [Ja/Belibige Nummer: Zurück]: ")
    if int(az0) == 1:
        var.zimmer = 0
    else:
        var.zimmer = 1

def interaktion20():
    az0=input("\nMit der Tür interagieren? [Ja/Belibige Nummer: Zurück]: ")
    if int(az0) == 1:
        var.zimmer = 0
    else:
        var.zimmer = 2

def haupt_interaktion():
    in1 = input("\nWas möchtest du tun? [1:Gehe zu / 2:Drehe dich / 3:Interagiere]: ")
    if in1 == "1":
        string = "Wohin magst du gehen? [1:"+var.verfügbare_Zimmer[0]+"/ 2:"+var.verfügbare_Zimmer[1]+"/ 3:"+var.verfügbare_Zimmer[2]+"]: "
        in2 = input(string)
        if (var.is_integer(in2)) == True:
            if int(in2) > 0 and int(in2) <= len(var.verfügbare_Zimmer):
                if (var.verfügbare_Zimmer[int(in2)-1] != "None"):
                    var.zimmer = int(in2)-1
                else:
                    print("\nIch weiss nicht, wo sich weitere Zimmer befinden.")
                    time.sleep(var.standardWait)
            else:
                print("\nIch kenne dieses Zimmer nicht.")
                time.sleep(var.standardWait)
    elif in1 == "2":
        in2 = input("In welche Richtung soll ich mich drehen? [1:Links / 2:Rechts]: ")
        if (var.is_integer(in2)) == True:
            if int(in2) == 1:
                var.richtung = var.richtung - 1
            if var.richtung < 0:
                var.richtung = 3
            if int(in2) == 2:
                var.richtung = var.richtung + 1
            if var.richtung > 3:
                var.richtung = 0
    elif in1 == "3":
        if var.zimmer == 0 and var.richtung == 0:
            z0.interaktion00()
        if var.zimmer == 0 and var.richtung == 1:
            z0.interaktion01()
        if var.zimmer == 0 and var.richtung == 2:
            z0.interaktion02()
        if var.zimmer == 0 and var.richtung == 3:
            z0.interaktion03()
        if var.zimmer == 1 and var.richtung == 0:
            z1.interaktion10()
        if var.zimmer == 1 and var.richtung == 1:
            z1.interaktion11()
        if var.zimmer == 1 and var.richtung == 2:
            z1.interaktion12()
        if var.zimmer == 1 and var.richtung == 3:
            interaktion13()
        if var.zimmer == 2 and var.richtung == 0:
            interaktion20()
        if var.zimmer == 2 and var.richtung == 1:
            z2.interaktion21()
        if var.zimmer == 2 and var.richtung == 2:
            z2.interaktion22()
        if var.zimmer == 2 and var.richtung == 3:
            z2.interaktion23()

## Spiel
inp_tutorial=input("Tutorial und Intro überspringen? [1: Nein /~: Überspringen]: ")
if inp_tutorial == "1":
    tutorial()
    intro()
os.system('cls||clear')
z0.arbeitszimmer_intro()
while var.loop == True:
    if var.zimmer == 0:
        z0.arbeitszimmer(var.richtung)
    elif var.zimmer == 1:
        z1.labor(var.richtung)
    elif var.zimmer == 2:
        z2.keller(var.richtung)
    haupt_interaktion()