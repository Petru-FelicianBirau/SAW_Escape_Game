import time
import os
from colorama import Fore, Back, Style 
import Material as mat
import keyboard
from playsound import playsound
import outro
import Variables as var
import zimmer1_lib as z1
import zimmer2_lib as z2

#Lochquiz:
time_pressD = 5
end_pressD = 50
lochQuiz = False
loop=True

notizen = ["Notizbuch:\n"]

def updateNotizen():
    global notizen
    notizen = ["Notizbuch:\n"]
    notizen_r = open('notizen.txt','r')
    for zeile in notizen_r:
        notizen.append(zeile)
    notizen_r.close()

def schreibeNotizen(inp):
    notizen_r = open('notizen.txt','r')
    temp=notizen_r.readlines()
    print(temp)
    notizen_r.close()
    notizen_w = open("notizen.txt","w")
    for zeile in temp:
        notizen_w.write(zeile)
    notizen_w.write("\n"+inp)
    notizen_w.close()

def loescheNotizen(inhalt):
    notizen_r = open("notizen.txt","r")
    temp = notizen_r.readlines()
    notizen_r.close()
    notizen_w = open("notizen.txt","w")
    for zeile in temp:
        if zeile != inhalt:
            notizen_w.write(zeile)
    notizen_w.close()

def arbeitszimmer_intro():
    print("\nIch befinde mich in einer Art Arbeitsszimmer.")
    print("Die Tapete an der Wand sind zerrissen und es herrscht Unordnung.")
    print("In den Schatten des roten, künstlichen Lichts macht sich eine massive Unordnung erkennbar.")

def arbeitszimmer(richtung: int):
    if richtung == 0:
        print("\nVor mir stehen ein Büro und ein alter Bücherschrank.")
        print("Sieht so aus, als wäre dies der Arbeitsplatz meines Entführers.")
        print("Seine Unordnung macht sich sichtbar.")
    if richtung == 1:
        print("\nIch stehe vor einer altmodischen Holztür.")
        print("Rechts und links sind 2 Bilder zu sehen.")
        print("Diese sind leicht schief angeordnet.")
    if richtung == 2:
        print("\nIch stehe vor einer massiven Eisentür mit einem Hebel.")
        print("Über dem Hebel sind zwei LEDs zu sehen.")
        print("Es scheint als würde sich ein Mechanismus dahinter verbergen.")
        print("Aber was löst dieses aus?")
    if richtung == 3:
        print("\nIch stehe vor einer massiven Eisentür.")
        print("Rechts ist ein Display mit Zahleneingaben zu sehen.")
        print("Der Mechanismus erscheint mir sehr komplex und schwer.")

def interaktion00():
    global end_pressD 
    global time_pressD 
    global lochQuiz
    global loop
    in1 = input("Womit soll ich interagieren? [1:Schreibtisch / 2:Schrank]: ")
    if in1 == "1":
        print("\nEs sind verschiedene Notizen und hängende Zeitungsartikeln zu sehen.")
        print("Unter anderem Berichte von einer Duzend vermisster Personen,")
        print("Anleitungen zum Bau verschiedener Bomben und unbekannte Baupläne für scheinbar mechanische Geräte.")
        in2 = input("\nWas möchtest du tun? [1:Vermisstenliste anschauen / 2:Zeitungsartikeln lesen / 3:Notiz schreiben / ~:Zurück]: ")
        if in2 == "1":
            i = int(0)
            while loop == True:
                os.system('cls||clear')
                mat.unknown()
                print("\n"+var.vl[i][0]+"\n")
                print(var.vl[i][1])
                in3=input("\nWeiter? [1: Ja / ~: Zurück]: ")
                if in3 == "1":
                    i=i+1
                    if i >= len(var.vl):
                        i=0
                else:
                    break
        elif in2 == "2":
            i = int(0)
            while loop == True:
                os.system('cls||clear')
                print(var.za[i][0])
                print(var.za[i][1])
                in3=input("\nWeiter? [1:Ja / ~: Zurück]: ")
                if in3 == "1":
                    i=i+1
                    if i >= len(var.za):
                        i=0
                else:
                    mat.cinema_Zeitungsartikel()
                    break
        elif in2 == "3":
            while loop == True:
                os.system('cls||clear')
                updateNotizen()
                i = int(0)
                while loop == True:
                    print(i,": ",notizen[i],end =""),
                    i=i+1
                    if i >= len(notizen):
                        break
                in3=input("\nUnd nun? [1:Neue Notiz verfassen / 2:Notiz löschen / ~: Zurück]: ")
                if in3 == "1":
                    in4=input("Notiz: ")
                    schreibeNotizen(in4)
                elif in3 == "2":
                    in4=input("Welche Notiz soll gelöscht werden? [Notiznummer / ~: Zurück]: ") 
                    if var.is_integer(in4) == True:
                        if int(in4) <= len(notizen) and int(in4) > 0:
                            string = notizen[int(in4)]
                            loescheNotizen(string)
                else:
                    break    
    if in1 == "2":
        print("\nEin moderner Schrank mit 13 Fächern, überraschenderweise im guten Zustand.")
        print("Dagegen sind die beinhaltete Bücher teilweise verbrannt und gerissen, kaum noch lesbar.")
        print("Es sind nurnoch einzelne Sätze und teilweise Wörter zu erkennen.")
        in2=input("\nWas möchtest du tun? [1:Bücher anschauen / 2:Schrank schieben / ~:Zurück]: ")
        if in2 == "1":
            while loop == True:
                os.system('cls||clear')
                i = int(0)
                while loop == True:
                    print(i+1,": ",var.buch_t[i])
                    i=i+1
                    if i >= len(var.buch_t):
                        break
                in3 = input("\nWelches Buch würdest du öffnen? [Buchnummer / ~: Zurück]: ")
                if var.is_integer(in3) == True:
                    if int(in3) <= len(var.buch_i) and int(in3) >= 0:
                        os.system('cls||clear')
                        print("Das Buch ist in sehr schlechtem Zustand, jedoch folgender Absatz ist noch lesbar.")
                        print("Komischerweise sind genau in diesem Absatz einige Buchstaben umkriengelt.\n")
                        print(var.buch_i[int(in3)-1])
                        input("\nKehre zurück? [Beliebige Eingabe]: ")
                    else:
                        break
        elif in2 == "2":
            print("\nEin dunkler, schmaler Gang offenbart sich.")
            print("Am Ende des Tunnels ist schwaches Licht zu sehen, das heißt da befindet sich etwas.")
            print("Jedoch ist der Weg dahin vollkommen im Dunkeln verborgen.")
            in3 = input("Was möchtest du tun? [1:Durch den Gang gehen / ~: Schrank zurückschieben]: ")
            if in3 == "1":
                if lochQuiz == False:
                    mat.cinema_lochQuiz()
                    temp_start = time.thread_time()
                    gescheitert = False
                    pressedD = 0
                    while loop == True:
                        os.system('cls||clear')
                        print("Tipp: Taste \"d\" drücken")
                        int_kraft = (time_pressD-(time.thread_time()-temp_start))*10
                        if int_kraft < 0:
                            int_kraft = 0
                        string_kraft = "█"
                        print("Zeit: ",int_kraft/10)
                        print("Kraft: ",int(int_kraft*(2/5))*string_kraft)
                        fortsc = int(pressedD/(end_pressD/20))
                        print("Fortschritt: ",fortsc*string_kraft)
                        if (time.thread_time()-temp_start) > time_pressD:
                            gescheitert = True
                        try:  
                            if keyboard.is_pressed('d'):
                                pressedD = pressedD + 1                         
                        except:
                            continue
                        if pressedD >= end_pressD:
                            lochQuiz = True
                            break
                        if gescheitert == True:
                            mat.death_Z0_lochQuiz()
                    print("Ich habe es geschafft!")
                    time.sleep(var.standardWait)
                    print("Außerdem bin ich auf einen Brett gestoßen.")
                    print("Damit habe ich das Loch verstopft und werde ab jetzt sicher hin und her laufen können.")
                    time.sleep(var.standardWait)
                print("\nIch bin im schlecht beleuchteten Raum angekommen.")
                print("Ich bin von lauter Ziegeln und Beton umgeben.")
                print("Es ist ein kleiner Raum mit nur einem Bild.")
                while loop == True:
                    in4 = input("\nWas möchtest du tun? [1:Bild verwalten / ~: Gehe zürück durch den Gang]: ")
                    if in4 == "1":
                        while loop == True:
                            os.system('cls||clear')
                            for i in range(0,9):
                                print("         ",mat.bilder_l[var.bild[2]][i])
                            in5 = input("In welche Richtung magst du das Bild drehen? [1:Uhrzeigersinn / 2:Entgegen /~: Zurück]: ")
                            if in5 == "1":
                                var.bild[2] = var.bild[2]+1
                                if var.bild[2] > 3:
                                    var.bild[2] = 0
                            elif in5 == "2":
                                var.bild[2] =var.bild[2]-1
                                if var.bild[2] < 0:
                                    var.bild[2] = 3
                            else:
                                break
                    else:
                        break

def interaktion01():
    in1 = input("Mit was soll ich interagieren? [1:Tür / 2:Bilder / ~: Zurück]: ")
    if in1 == "1":
        if var.verfügbare_Zimmer[1] == "None":
            in2 = input("Gehe durch die Tür? [1:Ja / 2:Nein]: ")
            if in2 == "1":
                var.verfügbare_Zimmer[1] = "Labor"
                var.zimmer = 1
                z1.labor_intro()
            else:
                var.zimmer = 0
        else:
            var.zimmer = 1
    elif in1 == "2":
        in2 = input("Was soll ich damit tun? [1:Bilder drehen / ~: Zurück]: ")
        if in2 == "1":
            while var.loop == True:
                os.system('cls||clear')
                for i in range(0,9):
                    print("         ",mat.bilder_l[var.bild[0]][i],"           ",mat.bilder_l[var.bild[1]][i])
                in4 = input("Welches Bild magst du drehen? [1:Linkes Bild / 2:Rechtes Bild / ~: Zurück]: ")
                if var.is_integer(in4) == True:
                    if int(in4) == 1 or int(in4) == 2:
                        in5 = input("Und welche Richtung? [1:Uhrzeigersinn / 2:Entgegen]: ")
                        if var.is_integer(in5) == True:
                            if int(in5) == 1:
                                rot = var.bild[int(in4)-1]+1
                                if rot > 3:
                                    rot = 0
                                var.bild[int(in4)-1] = rot
                            if int(in5) == 2:
                                rot = var.bild[int(in4)-1]-1
                                if rot < 0:
                                    rot = 3
                                var.bild[int(in4)-1] = rot
                else:
                    break

def interaktion02():
    if var.tur_offen == False:
        while var.loop == True:
            for i in range(3):
                if var.bild[i] == 0:
                    var.led[i] = 1
                    var.status_led[i] = Fore.GREEN
                else:
                    var.led[i] = 0
                    var.status_led[i] = Fore.RED 
            for i in range(5):
                if i != 2:
                    print(mat.hebel[i])
                else:
                    print(mat.hebel[i],var.status_led[0],"●",var.status_led[1],"●",var.status_led[2],"●",Fore.WHITE,mat.dot_end)
            in1 = input("\nSchalter betätigen? [1: Ja / ~: Nein]: ")
            if in1 == "1":
                if var.led[0]==1 and var.led[1]==1 and var.led[2]==1:
                    mat.cinema_Z0_Tür()
                    var.tur_offen = True
                    break
                else:
                    mat.death_Z0_Tür()
            else:
                break
    else:
        in1 = input("\nMit was soll ich interagieren? [1:Tür / 2:LED-Display / ~:Zurück]: ")
        if in1 == "1":
            if var.verfügbare_Zimmer[2] == "None":
                in2 = input("Gehe durch die Tür? [1:Ja / ~:Nein]: ")
                if in2 == "1":
                    var.verfügbare_Zimmer[2] = "Keller"
                    var.zimmer = 2
                    z2.keller_intro()
                else:
                    var.zimmer = 0
            else:
                var.zimmer = 2
        elif in1 == "2":
            for i in range(3):
                if var.bild[i] == 0:
                    var.led[i] = 1
                    var.status_led[i] = Fore.GREEN
                else:
                    var.led[i] = 0
                    var.status_led[i] = Fore.RED                    
            for i in range(5):
                if i != 2:
                    print(mat.hebel[i])
                else:
                    print(mat.hebel[i],var.status_led[0],"●",var.status_led[1],"●",var.status_led[2],"●",Fore.WHITE,mat.dot_end)
            in2 = input("\nSchalter betätigen? [1:Ja / ~:Nein]: ")
            if in2 == "2":
                print("Es ist nichts weiteres passiert...")
                time.sleep(var.standardWait)

def interaktion03():
    in1 = input("\nWomit soll ich interagieren? [1:Tür / 2:Mechanismus / ~: Zurück]: ")
    if in1 == "1":
        print("Die Tür is verschlossen...")
        print("Ich kann da nichts machen.")
        time.sleep(var.standardWait)
    elif in1 == "2":
        while var.loop == True:
            print("\nDas Mechanismus ist eine Folge von Zahlen, die man eingeben muss.")
            print("Ich kann eine bestimmte Zahl auswählen und verändern")
            print("Rechts davon befindet sich ein roter Knopf. Ob ich den drücken sollte?")
            print("\n     |",1,"|",2,"|",3,"|",4,"|",5,"|",6,"|",7,"|")
            print("     |",var.code[0],"|",var.code[1],"|",var.code[2],"|",var.code[3],"|",var.code[4],"|",var.code[5],"|",var.code[6],"|",Fore.RED,"  ●",Fore.WHITE)
            in2 = input("\nWie soll ich vorgehen? [1:Zahl eingeben / 2:Knopf drücken / ~: Zurück]: ")
            if in2 == "1":
                while var.loop == True:
                    os.system('cls||clear')
                    print("\n     |",1,"|",2,"|",3,"|",4,"|",5,"|",6,"|",7,"|")
                    print("     |",var.code[0],"|",var.code[1],"|",var.code[2],"|",var.code[3],"|",var.code[4],"|",var.code[5],"|",var.code[6],"|",Fore.RED,"  ●",Fore.WHITE)
                    in3 = input("\nWelche Zahl soll ich verändern? [Zahlposition aus der oberen Reihe aussuchen / ~: Zurück]: ")
                    if var.is_integer(in3) == True:
                        if int(in3) > 0 and int(in3) <= len(var.code):
                            in4 = input("Was soll ich dort eingeben? [Zahl, die eingefügt werden soll]: ")
                            output = int(in4)
                            var.code[int(in3)-1] = output
                        else:
                            break
            elif in2 == "2":
                gewonnen = True
                for k in range(len(var.code)):
                    if var.code[k] != var.code_lsg[k]:
                        gewonnen = False
                if gewonnen != True:
                    print("Ich warte...")
                    print("Es ist nichts passiert.")
                    time.sleep(var.standardWait)
                    break
                else:
                    outro.outro()
            else:
                break
            