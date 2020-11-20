import time
import os
import Variables as var
from playsound import playsound

def death_Bild():
    print("     ███████▀▀▀░░░░░░░▀▀▀███████")
    print("     ██████▀░░░░░░░░░░░░░░░▀████")
    print("     █████│░░░░░░░░░░░░░░░░│████")
    print("     ████└┐░░░░░░░░░░░░░░░┌┘░███")
    print("     ███░░└┐░░░░░░░░░░░░░░┌┘░░██")
    print("     ███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
    print("     ██▌░▄██████▄░░░▄██████▄░▐██")
    print("     ███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███")
    print("     ██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██")
    print("     ██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███")
    print("     ████▄─┘█████████████└─▄████")
    print("     █████░░▐███████████▌░░█████")
    print("     ██████░░▀█████████▀░░▐█████")
    print("     ███████░░░░▓▓▓▓▓░░░░▄██████")
    print("     ████████▄░░░░░░░░░▄████████")
    print("     ███████████▓▓▓▓▓███████████")
    print("     ███████████▓▓▓▓▓███████████\n")

def unknown():
    print("__________________ss$s$$s$$s$s")
    print("_______________s$$s$S$ss$$s$s$$s")
    print("____________s$$$$$s$ssssss____s$$")
    print("___________$s$$$s$$$$$$$s_$sss__$$")
    print("__________s$$ss$$$s$$$$$$sssss$$$$")
    print("___________s$$$s$s__s$___$s$$$$_$$")
    print("_____________s$s___s$ss__s$$s$$$$s")
    print("______________s$$s__s$______s$$$s")
    print("______________s$____________s$$")
    print("_______________s$ss$$s_____s_$")
    print("_________________$$$s____s___s$")
    print("___________________ss$$$s____s$$$s")
    print("__________________s$$$ss$s$ssssss$$$s")
    print("_____________s$$$s_s$sssssss________s$$")
    print("___________s$$s_________________s___$s$$")
    print("__________s$s________________s_____ss_s$$")
    print("_________s$$s________________s_____s___s$s")

def cinema_Z0_Tür():
    print("\nEin lauter Knall ist zu hören.")
    time.sleep(var.standardWait)
    print("Metall knurrt an Metall...")
    print("Ein Prozess ist im Gange...")
    time.sleep(var.standardWait)
    print("Und dann die Stille...")
    time.sleep(var.standardWait)
    print("Die massive Tür bewegt sich langsam und lässt einen kleinen Spalt offen!")
    time.sleep(var.standardWait)

def cinema_Zeitungsartikel():
    os.system('cls||clear')
    print("\nHmmmm... Das neueste Datum ist im Juli 2019.")
    print("Soweit ich weiß, bin ich am 11. Januar 2019 schlafen gegangen.")
    time.sleep(var.standardWait)
    print("Aber das müsste bedeuten, ich hätte über ein halbes Jahr geschlafen.")
    time.sleep(var.standardWait)
    print("Sowas ist unmöglich; irgendwas stimmt nicht...")
    time.sleep(var.standardWait)

def cinema_lochQuiz():
    print("\nIch taste mich langsam voran...")
    time.sleep(var.standardWait)
    print("Die Hälfte des Weges, habe ich schon geschafft...")
    time.sleep(var.standardWait)
    print("ARGHHHHH!!!")
    time.sleep(var.standardWait)
    print("Ich bin auf ein Loch gestoßen, und hänge nun an der Kante! Meine Arme werden immer schwächer!")
    time.sleep(var.standardWait)
    print("Ich muss all meine Kräfte zusammenreißen und mich hochziehen! Der Schmerz wird immer größer!")
    time.sleep(var.standardWait)

def death_Z0_Tür():
    os.system('cls||clear')
    print("Es war eine Falle!")
    time.sleep(var.standardWait)
    death_Bild()
    print("Die BOMBE IST HOCHGEGANGEN!")
    playsound("End.mp3")
    time.sleep(var.endWait)
    quit()

def death_Z0_lochQuiz():
    time.sleep(var.standardWait)
    os.system('cls||clear')
    print("Ich kann den Schmerz nicht länger ertragen!")
    time.sleep(var.standardWait)
    death_Bild()
    print("Du bist runtergefallen!")
    playsound("End.mp3")
    time.sleep(var.endWait)
    quit()
bilder_l = ["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""]

bilder_l[0][0]="█████████████████████"
bilder_l[0][1]="████████░░░░█████████"
bilder_l[0][2]="██████░░████░░███████"
bilder_l[0][3]="███████████░░████████"
bilder_l[0][4]="██████████░░█████████"
bilder_l[0][5]="███████████░░████████"
bilder_l[0][6]="██████░░████░░███████"
bilder_l[0][7]="████████░░░░█████████"
bilder_l[0][8]="█████████████████████"

bilder_l[1][0]="█████████████████████"
bilder_l[1][1]="█████████████████████"
bilder_l[1][2]="█████░░███████░░█████"
bilder_l[1][3]="███░░█████░█████░░███"
bilder_l[1][4]="███░░███░░█░░███░░███"
bilder_l[1][5]="█████░░░█████░░░█████"
bilder_l[1][6]="█████████████████████"
bilder_l[1][7]="█████████████████████"
bilder_l[1][8]="█████████████████████"

bilder_l[2][0]="█████████████████████"
bilder_l[2][1]="████████░░░░█████████"
bilder_l[2][2]="██████░░████░░███████"
bilder_l[2][3]="████████░░███████████"
bilder_l[2][4]="██████████░░█████████"
bilder_l[2][5]="████████░░███████████"
bilder_l[2][6]="██████░░████░░███████"
bilder_l[2][7]="████████░░░░█████████"
bilder_l[2][8]="█████████████████████"

bilder_l[3][0]="█████████████████████"
bilder_l[3][1]="█████████████████████"
bilder_l[3][2]="█████░░░█████░░░█████"
bilder_l[3][3]="███░░███░░█░░███░░███"
bilder_l[3][4]="███░░█████░█████░░███"
bilder_l[3][5]="█████░░███████░░█████"
bilder_l[3][6]="█████████████████████"
bilder_l[3][7]="█████████████████████"
bilder_l[3][8]="█████████████████████"

hebel = ["","","","",""]

hebel[0]="████████████████████████████"
hebel[1]="███░░░░░░███████████████████"
hebel[2]="████░██░████████"
hebel[3]="████░██░████████████████████"
hebel[4]="████████████████████████████"
dot_end= "█"

acht = ["","","","","","","","",""]

acht[0]="████████████████████"
acht[1]="██░█████░░░░█████░██"
acht[2]="██░███░░████░░███░██"
acht[3]="█░█████░░██░░█████░█"
acht[4]="█░███████░░███████░█"
acht[5]="█░█████░░██░░█████░█"
acht[6]="██░███░░████░░███░██"
acht[7]="██░█████░░░░█████░██"
acht[8]="████████████████████"