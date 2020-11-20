import time
import os
from colorama import Fore, Back, Style 
import Material as mat
from playsound import playsound
import Variables as var

filling = 5
maximale_auffüllung = 3
fluids = [filling,filling,filling,filling]
haupt = [1,1,1,1]
loop = True
chemie_gelöst = False
verh = 0
volt = [2.5,3.2,4.5,1.3,0.7,1.8]
resist_v = [10,20,50,100,200,300]
resist =[0,0,0,0,0,0,0]
min_ampere = 0.008
max_ampere = 0.022
elektronik_gelöst = False
elek_lsg = [[Fore.RED,Fore.RED,Fore.RED,Fore.RED,Fore.RED,Fore.GREEN,Fore.RED,Fore.GREEN],[Fore.RED,Fore.RED,Fore.RED,Fore.RED,Fore.GREEN,Fore.GREEN,Fore.RED,Fore.GREEN]]
matrix_schalter = [[0,1,0,0,1,0,1,0],
                [0,1,1,0,1,0,1,0],
                [1,0,0,1,1,0,1,0],
                [1,0,0,1,1,0,1,0],
                [1,0,0,1,1,0,1,1],
                [1,0,0,1,1,0,1,0],
                [1,1,0,0,1,1,1,0]]
matrix_lsg = [[0,0,0,1,1,0,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,0,1,1,0,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,1,0,0,1,0,0],
            [0,0,0,1,1,0,0,0]]
matrix_led = [[0,1,0,0,1,0,1,0],
            [0,1,1,0,1,0,1,0],
            [1,0,0,1,1,0,1,0],
            [1,0,0,1,1,0,1,0],
            [1,0,0,1,1,0,1,0],
            [1,0,0,1,1,0,1,1],
            [1,1,0,0,1,1,1,1]]
matrix_gelöst = False

puzzle = [0,1,2,3,4,5,6,7,8]
puzzle_gemischt = [0,0,0,0,0,0,0,0,0]

def labor_intro():
    print("\nIch befinde mich nun in einer Art Labor.")
    print("Überfüllt von laufenden Maschinen, und laute, mechanische Geräusche.")
    print("Die Stimmung ist aufgehetzt, so als würde man in Bewegung bleiben wollen.")
    print("Die Beleuchtung ist durch wechselhaften Farbänderung der Displays ständig im Wechsel.")
    print("Die Zeit bleibt ebenfalls nicht stehen.")
    print("Ich sollte mich nach einem Ausgang umschauen.\n")
    time.sleep(var.standardWait)

def labor(richtung: int):
    if richtung == 0:
        print("\nEine Riesenmaschine gefüllt mit Schaltern und LEDs füllt die ganze Wand.")
        print("Diese ist die einzig statische Maschine im ganzen Raum.")
        print("Stumm und still beleuchtet sie die Ecke des Raums.")
        print("Dabei entstehen Lichtspiele des grünen und roten Lichtspektrums.")
    if richtung == 1:
        print("\nVor mir sind zwei laufende Maschinen.")
        print("Links scheint ein elektronisches Gerät mit Schaltungen interagieren.")
        print("Es piepst immer wieder.")
        print("Rechts ist eine Maschine, wie aus einer Chemiefabrik.")
        print("Behälter mit verschiedenen Flüssigkeiten oder Gase sind zu sehen.")
        print("Die Displayanzeige überzeugt durch Komplexität.")
    if richtung == 2:
        print("\nWeitere Quests?.")
    if richtung == 3:
        print("\nDa befindet sich dir Tür zum Arbeitszimmer.")
        print("Ansonsten gibt es in diese Richtung nichts erwähnenswertes.")

def interaktion10():
    global matrix_lsg
    global matrix_schalter
    global matrix_gelöst
    in1=input("Mit dieser Maschine interragieren? [1: Ja / ~: Nein]: ")
    if in1 == "1":
        if matrix_gelöst == False:
            while loop == True:
                os.system('cls||clear')
                print("Es gibt eine Matrix aus 40 Schaltern und eine Matrix aus 40 LEDs.")
                print("Es scheint, als wäre jedes Schalter mit der dazugehörigen LED verbunden zu sein.")
                print("Eine Anleitung ist nicht zu finden.")
                print("Es gibt nur eine geklebte Notiz meines Entführers.")
                print("Dort ist seine Vorliebe zu sehen; eine weitere Zahlenfolge aus 5 Zahlen.")
                print("Was diese wohl zu bedeuten hat?")
                print("Notiz: 24 -> 36 -> 36 -> 24 -> 36 -> 36 -> 24")
                for k in range(7):
                    for i in range(8):
                        if matrix_schalter[k][i] == 0:
                            matrix_led[k][i]=Fore.RED
                        elif matrix_schalter[k][i] == 1:
                            matrix_led[k][i]=Fore.GREEN
                for k in range(7):
                    print("\nZeile",k,": ", end = "") 
                    for i in range(8):
                        print("|",matrix_schalter[k][i],Fore.WHITE, end = "") 
                        print(" | ",Fore.WHITE, end = " ")  
                    for i in range(8):  
                        print(matrix_led[k][i],"●",Fore.WHITE, end = "")       
                in2=input("\n\nWelchen Schalter soll ich betätigen? [Zeilennummer / ~: Zurück]: ")
                if var.is_integer(in2):
                    if int(in2) > 0 and int(in2) <= 7:
                        in3=input("An welcher Position in der Zeile? [LED-Nummer / ~: Zurück]: ")
                        if var.is_integer(in3) == True:
                            if int(in3) > 0 and int(in3) <= 8:
                                matrix_schalter[int(in2)-1][int(in3)-1]=(matrix_schalter[int(in2)-1][int(in3)-1]+1)%2
                                matrix_gelöst = True
                                for k in range(7):
                                    for i in range(8):
                                        if matrix_schalter[k][i] != matrix_lsg[k][i]:
                                            matrix_gelöst = False
                                if matrix_gelöst == True:
                                    print("\nEs scheint so, als wäre dies eine bildliche Darstellung einer Acht.")
                                    print("Warum aber ausgerechnet die Acht?")
                                    print("Es ist aber interessant zu wissen, was man alles mit einer Reihenfolge machen kann.")
                                    print("Mein Entführer muss gutes mathematisches Verständnis besitzen.")
                                    break
                    else:
                        break
        else:
            print("\nEs scheint so, als wäre dies eine bildliche Darstellung einer Acht.")
            print("Warum aber ausgerechnet die Acht?")
            print("Es ist aber interessant zu wissen, was man alles mit einer Reihenfolge machen kann.")
            print("Mein Entführer muss gutes mathematisches Verständnis besitzen.")

def interaktion11():
    global maximale_auffüllung
    global fluids
    global haupt
    global filling
    global chemie_gelöst
    global verh

    global volt
    global resist_v
    global resist
    global min_ampere
    global max_ampere
    global elektronik_gelöst
    global elek_lsg

    in1=input("Mit welcher Maschine magst du interragieren? [1:Links / 2:Rechts / ~: Zurück]: ")
    if in1 == "1":
        if elektronik_gelöst == False:
            while loop == True:
                os.system('cls||clear')
                print("In der Anleitung steht man habe verschiedene Baukästen mit Widerständen.")
                print("Es gibt fünf elektrische Leitungen, an denen eine bestimmte Spannung angelegt ist.")
                print("Diese führen nach rechts in die Zentralkammer der rechten Maschine, wo Zünder angeschlossen sind.")
                print("Die richtigen Widerstände müssen so eingesteckt werden, sodass:")
                print("     - Die Stromstärke: zwischen",min_ampere*1000,"und",max_ampere*1000,"mA liegt.")
                print("     - Widerstand 0 Ohm, bedeutet, dass kein Widerstand eingesteckt ist.\n")
                print("   ","BK 1:",resist_v[0],"Ω","  BK 2:",resist_v[1],"Ω","  BK 3:",resist_v[2],"Ω","  BK 4:",resist_v[3],"Ω","  BK 5:",resist_v[4],"Ω","  BK 6:",resist_v[5],"Ω\n")
                print("   ","U: ",volt[0],"     ",volt[1],"     ",volt[2],"     ",volt[3],"     ",volt[4],"     ",volt[5])
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","       ","|")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","       ","^")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","      ","| |")
                print("   ","R: ","Ω_1","     ","Ω_2","     ","Ω_3","     ","Ω_4","     ","Ω_5","   ","Ω_6 Ω_7")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","      ","| |")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","      "," v ")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","       ","|")
                print("   ","Z:  ","=>","      ","=>","      ","=>","      ","=>","      ","=>","      ","=>")
                print("   ","    ","|","       ","|","       ","|","       ","|","       ","|","       ","|")
                print("   ","   ","¯¯¯","     ","¯¯¯","     ","¯¯¯","     ","¯¯¯","     ","¯¯¯","     ","¯¯¯","\n")
                print("   ","Ω_1:",resist[0],"  Ω_2:",resist[1],"  Ω_3:",resist[2],"  Ω_4:",resist[3],"  Ω_5:",resist[4],"  Ω_6:",resist[5],"  Ω_7:",resist[6])
                in2=input("Aus welchem Baukasten magst du einen Widerstand nehmen? [Kastennummer / ~: Zurück]: ")
                if var.is_integer(in2) == True:
                    if int(in2) > 0 and int(in2) <= 6:
                        in3=input("Wo in der Schaltung soll dieser eingesteckt werden? [Widerstandsnummer / ~: Zurück]: ")
                        if var.is_integer(in3) == True and int(in3) > 0 and int(in3) <= 7:
                            resist[int(in3)-1] = resist_v[int(in2)-1]
                    else:
                        break
                else:
                    break
                for i in range(5):
                    if resist[i] != 0:
                        ampere=volt[i]/resist[i]
                        if min_ampere <= ampere and ampere <= max_ampere:
                            continue
                        else:
                            os.system('cls||clear')
                            print("Die Zentralkammer wurde gezündet!")
                            time.sleep(var.standardWait)
                            mat.death_Bild()
                            print("Du bist durch Explosion gestorben!")
                            playsound("End.mp3")
                            time.sleep(var.endWait)
                            quit()
                    if (resist[5]+resist[6]) == resist[5] or (resist[5]+resist[6]) == resist[6]:
                        if resist[5]+resist[6] != 0:
                            ampere=volt[5]/(resist[5]+resist[6])
                            if min_ampere <= ampere and ampere <= max_ampere:
                                continue
                            else:
                                os.system('cls||clear')
                                print("Die Zentralkammer wurde gezündet!")
                                time.sleep(var.standardWait)
                                mat.death_Bild()
                                print("Du bist durch Explosion gestorben!")
                                playsound("End.mp3")
                                time.sleep(var.endWait)
                                quit()
                    else:
                        if resist[5]+resist[6] != 0:
                            ampere=volt[5]/((resist[5]*resist[6])/(resist[5]+resist[6]))
                            if min_ampere <= ampere and ampere <= max_ampere:
                                continue
                            else:
                                os.system('cls||clear')
                                print("Die Zentralkammer wurde gezündet!")
                                time.sleep(var.standardWait)
                                mat.death_Bild()
                                print("Du bist durch Explosion gestorben!")
                                playsound("End.mp3")
                                time.sleep(var.endWait)
                                quit()
                elektronik_gelöst = True
                for i in range(7):
                    if resist[i] == 0:
                        elektronik_gelöst = False
                if elektronik_gelöst == True:
                    print("Sieht gut aus! Alle Leitungen sind aktiv.\n")
                    print("Folgende binäre Ausgaben aus 8 LEDS ist zu Lesen:") 
                    for i in range(8):  
                        print(elek_lsg[0][i],"●",Fore.WHITE, end = " ") 
                    print("")
                    for i in range(8):  
                        print(elek_lsg[1][i],"●",Fore.WHITE, end = " ")  
                    input("\nBeliebige Eingabe, um zu verlasen: ")
                    break
        else:
            print("Folgende binäre Ausgaben aus 8 LEDS ist zu Lesen:") 
            for i in range(8):  
                print(elek_lsg[0][i],"●",Fore.WHITE, end = " ") 
            print("")
            for i in range(8):  
                print(elek_lsg[1][i],"●",Fore.WHITE, end = " ")  
            input("\nBeliebige Eingabe, um zu verlassen: ")
    elif in1 == "2":
        if chemie_gelöst == False:
            while loop == True:
                os.system('cls||clear')
                print("")
                print("In der Anleitung steht man habe verschiedene Gase: Sauerstoff, Wasserstoff und zwei Unbekannte.")
                print("Man kann immer eine gleiche Portion des Gases in die Hauptkammer führen.")
                print("Dabei darf man nicht mehr Sauerstoff wie Wasserstoff einführen, ansonst kann es zur Reaktion kommen.")
                print("Es sei denn, man führt eine der unbekannten Substanzen, die diese Reaktion neutralisiert.")
                print("Die andere Substanz dagegen, fungiert als Katalysator.\n")
                print("Behälter ",(1),": ",Fore.GREEN,fluids[0]*2*"█",Fore.WHITE)
                print("Behälter ",(2),": ",Fore.BLUE,fluids[1]*2*"█",Fore.WHITE)
                print("Behälter ",(3),": ",Fore.WHITE,fluids[2]*2*"█",Fore.WHITE)
                print("Behälter ",(4),": ",Fore.RED,fluids[3]*2*"█",Fore.WHITE,"\n")
                print("Zentral: ",Fore.GREEN,haupt[0]*"█",Fore.BLUE,haupt[1]*"█",Fore.WHITE,haupt[2]*"█",Fore.RED,haupt[3]*"█",Fore.WHITE)
                print("\nStatus: ",maximale_auffüllung*2*"█ ")
                print("\nRef: ", round(verh,2))
                in2=input("\nWelche Substanz magst du einleiten? [Nummer des Behälters / ~: Zurück]: ")
                if var.is_integer(in2) and int(in2) > 0 and int(in2) <= 4:
                    fluids[int(in2)-1]=fluids[int(in2)-1]-1
                    if fluids[int(in2)-1] <= 0:
                        fluids[int(in2)-1] = filling
                        maximale_auffüllung = maximale_auffüllung-1
                        if maximale_auffüllung <= 0:
                            os.system('cls||clear')
                            print("Der Druck in der Zentralkammer ist zu stark abgestiegen!")
                            time.sleep(var.standardWait)
                            print("Die Ventile haben nachgelassen, zu viel Sauerstoff ist in die Hauptkammer geflossen!")
                            time.sleep(var.standardWait)
                            mat.death_Bild()
                            print("Du bist durch Explosion gestorben!")
                            playsound("End.mp3")
                            time.sleep(var.endWait)
                            quit()
                    haupt[int(in2)-1]=haupt[int(in2)-1]+1
                    if (haupt[3] - haupt[1]) > (0 + haupt[0] - haupt[2]):
                        os.system('cls||clear')
                        print("Du hast zu viel Sauerstoff verwendet!")
                        time.sleep(var.standardWait)
                        mat.death_Bild()
                        print("Du bist durch Explosion gestorben!")
                        playsound("End.mp3")
                        time.sleep(var.endWait)
                        quit()
                    verh = (haupt[3] / haupt[1])
                    if verh >= 2.1:
                        print("Ich glaube ich habe die richtigen Einstellungen erwischt!")
                        time.sleep(var.standardWait)
                        print("\nEs hat sich eine kleine Schacht geöffnet.")
                        print("Dort sind 13 Zahlen eingraviert.")
                        print("Sieht so aus, als hätte mein Entführer eine Vorliebe für mathematische Folgen.")
                        print("Ich kann aber die Zahlenfolge nicht einreihen, weil die Zahlen durcheinander sind.")
                        print("Das spiegelt seine Unordnung wieder.")
                        print("Jedoch ist die Zahl 13 hervorgehoben, so als würde sie eine wichtige Rolle spielen.\n")
                        input("Beliebige Eingabe, um die Schacht zu schliessen: ")
                        chemie_gelöst = True
                        break
                else:
                    break
        else:
            print("\nEs hat sich eine kleine Schacht geöffnet.")
            print("Dort sind 13 Zahlen eingraviert.")
            print("Sieht so aus, als hätte mein Entführer eine Vorliebe für mathematische Folgen.")
            print("Ich kann aber die Zahlenfolge nicht einreihen, weil die Zahlen durcheinander sind.")
            print("Das spiegelt seine Unordnung wieder.")
            print("Jedoch ist die Zahl 13 hervorgehoben, so als würde sie eine wichtige Rolle spielen.\n")
            input("Beliebige Eingabe, um die Schacht zu schliessen: ")

def interaktion12():
    in1=input("Womit magst du interragieren? [1: Puzzle / / ~: Zurück]: ")
    if in1 == "1":
        print("hi")


def interaktion13():
    in1=input("\nMit der Tür interagieren? [1:Ja / ~: Zurück]: ")
    if in1 == "1":
        var.zimmer = 0
    else:
        var.zimmer = 1