import time
import os
from colorama import Fore, Back, Style 
import Material as mat
from playsound import playsound
import Variables as var
import Material as mat
import threading as th
import sys
import msvcrt

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
puzzle_gemischt = [4,3,6,2,1,0,8,5,7]
puzzle_gelöst = False
kamin_offen = False
kamin_Quiz = False
#Kabelsalat Farbe[Leitung],Typ[mit Zünder?],Verbunden?
kabelsalat = [Fore.BLUE,1,0],[Fore.RED,0,1],[Fore.GREEN,0,1],[Fore.GREEN,1,1],[Fore.RED,1,1],[Fore.GREEN,0,0]
kabel = [[">>----//------------O"],[">>------------------O"]],[[">>----//----|^|-----O"],[">>----------|^|-----O"]]
print_cooldown = False
defused = False

def labor_intro():
    print("\nIch befinde mich nun in einer Art Labor.")
    print("Überfüllt von laufenden Maschinen, und laute, mechanische Geräusche.")
    print("Die Stimmung ist aufgehetzt, so als würde man in Bewegung bleiben wollen.")
    print("Die Beleuchtung ist durch wechselhaften Farbänderung der Displays ständig im Wechsel.")
    print("Die Zeit bleibt ebenfalls nicht stehen.")
    print("Ich sollte mich nach einem Ausgang umschauen.\n")
    time.sleep(var.standardWait)

def labor(richtung: int):
    global kamin_offen
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
        if kamin_offen == False:
            print("\nEs wird heiß. Vor mir befindet sich eine angezündete Feuerstelle.")
            print("Der Brennstoff geht jedoch bald leer.")
            print("Neben dem klassischen Ziegelkamin, steht ein Tisch im viktorianischem Stil.")
            print("Darauf ist eine Art Puzzle zu sehen.")
            print("Es sieht so aus, als wäre dies ein persönlicher Resort des Entführers.")
        else:
            print("\nVor mir befindet sich eine Feuerstelle.")
            print("Der Brennstoff ist vollständig verbrannt.")
            print("Seitlich am Kamin ist eine menschensgroße Öffnung in der Wand.")
            print("Neben dem klassischen Ziegelkamin, steht ein Tisch im viktorianischem Stil.")
            print("Darauf ist eine Art Puzzle zu sehen.")
            print("Es sieht so aus, als wäre dies ein persönlicher Resort des Entführers.")
    if richtung == 3:
        print("\nDa befindet sich dir Tür zum Arbeitszimmer.")
        print("Außer massive Risse in der Wand, gibt es in diese Richtung nichts erwähnenswertes.")

def countdown(delay, times):
    t=times
    s=time.time_ns()*10**(-9)
    while t-((time.time_ns()*10**(-9) - s)) > 0:
        tc = t-((time.time_ns()*10**(-9) - s))
        if print_cooldown == True:
            if tc >= 10:
                os.system('cls||clear')
                print("\n   [",Fore.RED,"00:"+str(round(tc)),Fore.WHITE,"]")
                print("Drücke beliebige Taste um zu schließen.")
            else:
                os.system('cls||clear')
                print("\n   [",Fore.RED,"00:0"+str(round(tc)),Fore.WHITE,"]")
                print("Drücke beliebige Taste um zu schließen.")
        time.sleep(float(delay))
    return(42)

def bombDeath():
    os.system('cls||clear')
    print("Die Bombe ist explodiert!")
    mat.death_Bild()
    playsound("End.mp3")
    time.sleep(2)
    os._exit(1)
    
def münzeDeath():
    os.system('cls||clear')
    print("Du hast zu lange gebraucht, um zu überlegen!")
    print("Der ganze Raum ist kollabiert!")
    mat.death_Bild()
    playsound("End.mp3")
    time.sleep(2)
    os._exit(1)

def kollapsDeath():
    os.system('cls||clear')
    print("Du hast es nicht geschafft!")
    mat.death_Bild()
    playsound("End.mp3")
    time.sleep(var.endWait)
    os._exit(1)

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
    global puzzle_gelöst
    global kamin_offen
    global kamin_Quiz
    global puzzle
    global puzzle_gemischt
    global kabelsalat
    global kabel
    global print_cooldown
    global defused
   
    in1=input("Womit magst du interragieren? [1: Puzzle / 2:Feuerstelle / ~: Zurück]: ")
    if in1 == "1":
        if puzzle_gelöst == False:
            while var.loop == True:
                os.system('cls||clear')
                print("Folgender Puzzle ist zu lösen:\n")
                for i in range(len(puzzle)):
                    print(" Zeile: ",i+1,"    ",mat.acht[puzzle_gemischt[i]])
                in2=input("\nWelche Zeile magst du auswählen? [Zeilennummer / ~:Zurück]: ")
                if var.is_integer(in2) == True:
                    if int(in2) > 0 and int(in2) <= len(puzzle_gemischt):
                        in3=input("Mit welcher Zeile magst du diese austauschen? [Zeilennummer / ~:Zurück]: ")
                        if var.is_integer(in3) == True:
                            if int(in3) > 0 and int(in3) <= len(puzzle_gemischt):
                                temp = puzzle_gemischt[int(in3)-1]
                                puzzle_gemischt[int(in3)-1] = puzzle_gemischt[int(in2)-1]
                                puzzle_gemischt[int(in2)-1] = temp
                    else:
                        break
                else:
                    break
                puzzle_gelöst = True
                for i in range(len(puzzle)):
                    if puzzle_gemischt[i] == puzzle[i] or puzzle_gemischt[i] == puzzle[len(puzzle)-i-1]:
                        continue
                    else:
                        puzzle_gelöst = False
                if puzzle_gelöst == True:
                    kamin_offen = True
                    print("\nDer Boden unter mir vibriert!")
                    time.sleep(var.standardWait)
                    print("Die Wände zittern und das Kamin rutsch langsam auf den Fliesen.")
                    time.sleep(var.standardWait)
                    print("Ein Tunnel offenbart sich auf der rechten Seite der Feuerstelle.")
                    time.sleep(var.standardWait)
                    print("Es sieht aus, als würde sich dort ein Geheimgang verstecken.")
                    time.sleep(var.standardWait)
        else:
            print("\nDen Puzzle habe ich schon gelöst.")
            print("Das Bild war eine Acht; oder je nach Betrachtung das Zeichen für Unendlich.")
            print("Ich frage mich immer wieder, ob die ganze Zahlen in der Wohnung eine Bedeutung haben.")
            input("Beliebige Taste, um Puzzle zu verlassen: ")
    elif in1 == "2":
        if kamin_offen == True:
            in2=input("Möchtest du hineingehen? [1:Ja / ~:Nein]: ")
            if in2 == "1":
                if kamin_Quiz == False:
                    print("\nDann los geht\'s... Yaay *sarkastisch*...")
                    time.sleep(var.standardWait)
                    print("Es ist eine Art Tunnelsystem...")
                    time.sleep(var.standardWait)
                    print("Umgegeben von schlechtem Licht und Beton, taste ich mich langsam voran...")
                    time.sleep(var.standardWait)
                    print("Wenn man das Labor verlässt, weiß man die Stille zu genießen...")
                    time.sleep(var.standardWait)
                    print("Ich bin an einer Kreuzung angekommen.")
                    in3=input("\nSoll ich den rechten oder linken Gang nehmen? [1:Links / 2:Rechts /~: Zurück]: ")
                    if in3 == "1":
                        print("\nSoweit sogut...")
                        time.sleep(var.standardWait)
                        print("Mir fällt aber etwas ein...")
                        time.sleep(var.standardWait)
                        print("Das Feuer!")
                        time.sleep(var.standardWait)
                        print("Wenn das Holz noch nicht ganz verbrannt war...")
                        time.sleep(var.standardWait)
                        print("Musste doch jemand vor Kurzem Holz drauf gelegt haben...")
                        time.sleep(var.standardWait)
                        print("Könnte mein Entführer noch in der Nähe sein?!")
                        time.sleep(var.standardWait)
                        print("Na, toll! Eine weitere Gabelung!")
                        time.sleep(var.standardWait)
                        in4=input("\nSoll ich den rechten oder linken Gang nehmen? [1:Links / 2:Rechts /~: Zurück]: ")
                        if in4 == "1":
                            print("\nIch hoffe es erwarten mich keine Überraschungen.")
                            time.sleep(var.standardWait)
                            print("Warum wurden Professoren und Wissenschaftler entführt?")
                            time.sleep(var.standardWait)
                            print("Wie passe ICH im Gesamtbild? Ich habe mit den anderen nichts gemeinsam.")
                            time.sleep(var.standardWait)
                            print("Was hat mein Entführer überhaupt vor?")
                            time.sleep(var.standardWait)
                            print("So viele Fragen...")
                            time.sleep(var.standardWait)
                            print("Wenn ich aus diesem Loch rauskomme und in Sicherheit bin, habe ich mehr Zeit nachzudenken...")
                            time.sleep(var.standardWait)
                            print("Da ist schon die nächste Kreuzung.")
                            in5=input("\nWelchen Gang soll ich nehmen? [1:Links / 2:Rechts / 3:Geradeaus /~: Zurück]: ")
                            if in5 == "1":
                                if defused == False:
                                    print("Ich habe das Gefühl es kommt eine Sackgasse.")
                                    time.sleep(var.standardWait)
                                    print("Da! Ich hatte Recht.")
                                    time.sleep(var.standardWait)
                                    print("*Knuuuuurr* *Piep piep*")
                                    time.sleep(var.standardWait)
                                    print("Der Tunnel hinter mir hat sich schlagartig geschlossen.")
                                    time.sleep(var.standardWait)
                                    print("Rechts ist auf Einmal ein piepsen zu hören.")
                                    time.sleep(var.standardWait)
                                    print("Ich gehe nachschauen...")
                                    time.sleep(var.standardWait)
                                    bomb_time = 30
                                    T = th.Timer(bomb_time, bombDeath)
                                    T.start()
                                    T2 = th.Thread(target=countdown,args=(0.5,bomb_time))
                                    T2.start()
                                else:
                                    print("\nDa war die Bombe...")
                                    time.sleep(var.standardWait)
                                    print("Es ist immernoch eine Sackgasse...")
                                    time.sleep(var.standardWait)
                                    print("Ich gehe mich aufwärmen im Labor.")
                                    time.sleep(var.standardWait)
                                while defused == False:
                                    os.system('cls||clear')
                                    print("\nIch stehe vor einer tickenden Bombe!!!")
                                    inb = input("Was soll ich tun? [1:Kabel / 2:Display /~: Zurück]: ")
                                    if inb == "1":
                                        while var.loop == True:
                                            os.system('cls||clear')
                                            print("")
                                            for i in range(len(kabelsalat)):
                                                print("Option",i+1,":  ",kabelsalat[i][0],kabel[kabelsalat[i][1]][kabelsalat[i][2]],Fore.WHITE)
                                            print("\nIch kann die Kabel nur wieder verbinden oder trennen.")
                                            inb2=input("Welche Leitung darf ich ändern? Vorsichtig! [Optionsnummer eingeben / ~:Zurück]: ")
                                            if var.is_integer(inb2):
                                                if int(inb2) > 0 and int(inb2) <= len(kabelsalat):
                                                    kabelsalat[int(inb2)-1][2] = (kabelsalat[int(inb2)-1][2]+1)%2
                                                else:
                                                    break
                                            else:
                                                break
                                            if kabelsalat[0][2] == 1 or kabelsalat[1][2] == 0 or kabelsalat[4][2] == 0:
                                                bombDeath()
                                            if kabelsalat[3][2] == 0 and kabelsalat[5][2] == 0 and kabelsalat[2][2] == 0:
                                                bombDeath()
                                            if kabelsalat[3][2] == 0:
                                                T.cancel()
                                                os.system('cls||clear')
                                                print("\nDu hast den Richtigen erwischt!")
                                                defused = True
                                                time.sleep(3)
                                                break
                                    elif inb == "2":                                
                                        while var.loop == True:
                                            print_cooldown = True
                                            if msvcrt.kbhit():
                                                print_cooldown = False
                                                break
                            elif in5 == "2":
                                print("\nIch sollte mir auf jeden Fall den Weg zurück merken.")
                                time.sleep(var.standardWait)
                                print("Links, Links, Rechts...")
                                time.sleep(var.standardWait)
                                print("Soweit noch alles einfach...")
                                time.sleep(var.standardWait)
                                print("Doch ich muss wachsam bleiben...")
                                time.sleep(var.standardWait)
                                print("Wach sein, ist das wesentliche...")
                                time.sleep(var.standardWait)
                                print("Da weiß man wie sich das Leben anfühlt...")
                                time.sleep(var.standardWait)
                                print("Ist es körperlich möglich, dass ein Mensch monatelang schläft?")
                                time.sleep(var.standardWait)
                                print("Persönliche Meinung? Schwachsinn...")
                                time.sleep(var.standardWait)
                                print("Es ist eine Frage für die Wissenschaft. Ich kenne da keine Antwort...")
                                time.sleep(var.standardWait)
                                print("Was für eine Überraschung! Der Weg spaltet sich erneut")
                                time.sleep(var.standardWait)
                                in6=input("\nNa dann los, was kann schon passieren? [1:Links / 2:Rechts / 3:Geradeaus /~: Zurück]: ")
                                if in6 == "1":
                                    print("\nHmmmm...")
                                    time.sleep(var.standardWait)
                                    print("Wenn ich eine Voraussage machen müsste...")
                                    time.sleep(var.standardWait)
                                    print("Würde ich sagen, ich laufe auf eine Sackgasse hin...")
                                    time.sleep(var.standardWait)
                                    print("3, 2, 1... Sackgasse.")
                                    time.sleep(var.standardWait)
                                    print("Ich sollte zum Labor zurückkehren bevor ich mich richtig verlaufe!")
                                    time.sleep(var.standardWait)
                                elif in6 == "2":
                                    print("\nIch stelle mir immer wieder die Frage...")
                                    time.sleep(var.standardWait)
                                    print("Ob sich hier ein Schatz verbirgt...")
                                    time.sleep(var.standardWait)
                                    print("Das würde mein Tag machen...")
                                    time.sleep(var.standardWait)
                                    print("Aber, es ist ein Dead End.")
                                    time.sleep(var.standardWait)
                                    print("Ich sollte mich weiter im Labor umschauen. Muss hier raus.")
                                    time.sleep(var.standardWait)
                                elif in6 == "3":
                                    print("\nHmmmm...")
                                    time.sleep(var.standardWait)
                                    print("Wenn ich meinen Verstand nicht selber hinterfragen würde...")
                                    time.sleep(var.standardWait)
                                    print("Würde ich sagen, es wird immer heller...")
                                    time.sleep(var.standardWait)
                                    print("Habe ich einen Ausgang gefunden?")
                                    time.sleep(var.standardWait)
                                    print("Ich bin da...")
                                    time.sleep(var.standardWait)
                                    kamin_Quiz = True
                                    print("\nEs ist ein Schatz! Ich habe einen Schatz gefunden!")
                                    time.sleep(var.standardWait)
                                    print("Vor mir sind vier Schalen mit Goldmünzen.")
                                    time.sleep(var.standardWait)
                                    print("Zwei beinhalten eine, eine Schale beinhaltet zwei und die letzte drei Münzen!")
                                    time.sleep(var.standardWait)
                                    print("Ob das was zu bedeuten hat?")
                                    time.sleep(var.standardWait)
                                    in7=input("\nSoll ich gierig sein und die Münzen mitnehmen? [1:Ja / ~:Gehe zum Labor zurück]: ")
                                    if in7 == "1":
                                        print("\nDer ganze Tunnel bebt!!!!")
                                        time.sleep(var.standardWait)
                                        print("Ich sollte die Münze nie genommen haben!!!!")
                                        time.sleep(var.standardWait)
                                        print("Ich weiß nicht, ob es was bringt, wenn ich die Münze zurückmache.")
                                        time.sleep(var.standardWait)
                                        print("Oder sollte ich so schnell ich kann zum Labor rennen??!!")
                                        time.sleep(var.standardWait)
                                        T3 = th.Timer(7, münzeDeath)
                                        T3.start()
                                        in8=input("\nWAS TUN?!?! [1:Münze zurück / ~:RENN]: ")
                                        if in8 == "1":
                                            T3.cancel()
                                            print("\nDas Beben...")
                                            time.sleep(var.standardWait)
                                            print("Hat aufgehört!")
                                            time.sleep(var.standardWait)
                                            print("Ich weiß nicht, ob ich es überhaupt geschafft hätte zum Labor.")
                                            time.sleep(var.standardWait)
                                            print("Ich habe die richtigen Entscheidung getroffen.")
                                            time.sleep(var.standardWait)
                                            print("Aber jetzt sollte ich zum Labor gehen. Ich muss weiterhin einen Ausgang finden.")
                                            time.sleep(var.standardWait)
                                        else:
                                            T3.cancel()
                                            print("\nICH RENNE...")
                                            time.sleep(var.standardWait)
                                            print("So schnell ich kann...")
                                            time.sleep(var.standardWait)
                                            print("Alles kollabiert!!")
                                            time.sleep(var.standardWait)
                                            print("Ich habe es fast geschafft!")
                                            time.sleep(var.standardWait)
                                            print("ARRRRGH!! Ein Stein!")
                                            time.sleep(var.standardWait)
                                            kollapsDeath()
                            elif in5 == "3":
                                print("\nDer Tunnel! Etwas stimmt hier nicht...")
                                time.sleep(var.standardWait)
                                print("Der Tunnel wird mit jedem Schritt schmaler...")
                                time.sleep(var.standardWait)
                                print("Ich muss langsam in der Hocke laufen...")
                                time.sleep(var.standardWait)
                                print("Ich kann leider nicht weiterlaufen...")
                                time.sleep(var.standardWait)
                                print("Meine Intuition sagt mir ich sollte nicht hier sein...")
                                time.sleep(var.standardWait)
                                print("Ich habe Angst um mein Leben...")
                                time.sleep(var.standardWait)
                                print("Ich muss raus aus dem Tunnel, bevor ich durchdrehe.")
                                time.sleep(var.standardWait)
                        elif in4 == "2":
                            print("\nDa wir von Feuer sprechen. Es wird irgendwie immer heißer...")
                            time.sleep(var.standardWait)
                            print("Ich glaube jemand hat vergessen die Klimaanlage anzumachen *Grins*.")
                            time.sleep(var.standardWait)
                            print("Die Hitze erschöpft mich...")
                            time.sleep(var.standardWait)
                            print("Eine Sackgasse! Ich brauche kurz eine Abkühlung...")
                            time.sleep(var.standardWait)
                            print("Ich kehre zum Labor zurück.")
                            time.sleep(var.standardWait)
                    elif in3 == "2":
                        print("\nIch weiß nicht, ob ich mich über die Einsamkeit freuen soll...")
                        time.sleep(var.standardWait)
                        print("Streng genommen, befinde ich mich auf feindlichem Gebiet...")
                        time.sleep(var.standardWait)
                        print("Ist es aber die Stille vor dem Krieg...")
                        time.sleep(var.standardWait)
                        print("Oder einfach nur Stille?")
                        time.sleep(var.standardWait)
                        print("Der Tunnel endet hier.")
                        time.sleep(var.standardWait)
                        print("Es gibt hier nichts zu tun. Ich kehre zum Labor zurück")
                        time.sleep(var.standardWait)
                else:
                    print("\nAußer vielen Sackgassen, gibt es nur den Schatzraum!")
                    time.sleep(var.standardWait)
                    print("Vor mir sind vier Schalen mit Goldmünzen.")
                    time.sleep(var.standardWait)
                    print("Zwei beinhalten eine, eine Schale beinhaltet zwei und die letzte drei Münzen!")
                    time.sleep(var.standardWait)
                    print("Ob das was zu bedeuten hat?")
                    time.sleep(var.standardWait)
                    in7=input("\nSoll ich gierig sein und die Münzen mitnehmen? [1:Ja / ~:Gehe zum Labor zurück]: ")
                    if in7 == "1":
                        print("\nDer ganze Tunnel bebt!!!!")
                        time.sleep(var.standardWait)
                        print("Ich sollte die Münze nie genommen haben!!!!")
                        time.sleep(var.standardWait)
                        print("Ich weiß nicht, ob es was bringt, wenn ich die Münze zurückmache.")
                        time.sleep(var.standardWait)
                        print("Oder sollte ich so schnell ich kann zum Labor rennen??!!")
                        time.sleep(var.standardWait)
                        T3 = th.Timer(7, münzeDeath)
                        T3.start()
                        in8=input("\nWAS TUN?!?! [1:Münze zurück / ~:RENN]: ")
                        if in8 == "1":
                            T3.cancel()
                            print("\nDas Beben...")
                            time.sleep(var.standardWait)
                            print("Hat aufgehört!")
                            time.sleep(var.standardWait)
                            print("Ich weiß nicht, ob ich es überhaupt geschafft hätte zum Labor.")
                            time.sleep(var.standardWait)
                            print("Ich habe die richtigen Entscheidung getroffen.")
                            time.sleep(var.standardWait)
                            print("Aber jetzt sollte ich zum Labor gehen. Ich muss weiterhin einen Ausgang finden.")
                            time.sleep(var.standardWait)
                        else:
                            T3.cancel()
                            print("\nICH RENNE...")
                            time.sleep(var.standardWait)
                            print("So schnell ich kann...")
                            time.sleep(var.standardWait)
                            print("Alles kollabiert!!")
                            time.sleep(var.standardWait)
                            print("Ich habe es fast geschafft!")
                            time.sleep(var.standardWait)
                            print("ARRRRGH!! Ein Stein!")
                            time.sleep(var.standardWait)
                            kollapsDeath()
        else:
            print("Der Kamin ist sehr heiß. Ich sollte ihn lieber nicht anfassen.")
            time.sleep(var.standardWait)

def interaktion13():
    in1=input("\nMit der Tür interagieren? [1:Ja / ~: Zurück]: ")
    if in1 == "1":
        var.zimmer = 0
    else:
        var.zimmer = 1