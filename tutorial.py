def tutorial():
    import time
    import os
    from colorama import Fore, Back, Style 
    from playsound import playsound

    os.system('cls||clear')

    endWait = 5
    standardWait = 2
    loop = True
    kabelsalat = False
    verlasse_schalter=False

    statuslinks_kabelsalat = [Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW]
    statusrechts_kabelsalat = [Fore.GREEN,Fore.YELLOW,Fore.RED,Fore.BLUE]
    status_verbindung = [Fore.BLACK,Fore.BLACK,Fore.BLACK,Fore.BLACK]
    verbindungen = [[0,2],[1,3],[2,4],[3,4]]
    loesung = [[0,2], [1,0], [2,3], [3,1]]

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

    def update_schalter():
        status_verbindung = [Fore.BLACK,Fore.BLACK,Fore.BLACK,Fore.BLACK]
        for i in range(0,4):
            if verbindungen[i][1]<4 and verbindungen[i][1]>-1:
                status_verbindung[verbindungen[i][1]] = statuslinks_kabelsalat[verbindungen[i][0]]
        
        for i in range(0,4):
            print(Fore.WHITE,i," :",statuslinks_kabelsalat[i]+"> === ", status_verbindung[i],"=== >", Fore.WHITE ," :", statusrechts_kabelsalat[i],"o",Fore.WHITE," :",i,Fore.WHITE )

    print("Tipp: geben sie für jede der Optionen, dessen Position als Integerzahl ein, um diese auszuführen \n \n")
    time.sleep(standardWait)
    print("Meine Augelieder öffnen sich und offenbaren einen dunklen Raum. ")
    time.sleep(standardWait)
    print("Erstmals ist alles verschwommen und unklar. ")
    time.sleep(standardWait)
    print("Doch langsam gewöhnen sich meine Pupillen an der Dunkelheit und erste Konturen nehmen Form. \n")
    time.sleep(standardWait)

    while loop == True:
        print("\nIch stehe vor einem Schalter mit einem Kabelsalat daneben. Der Schalter ist nach unten gerichtet")
        print("Rechts davon ein rotleuchtender Timer, die LED-Anzeige jedoch so kaputt, dass man kaum was erkennen kann")
        time.sleep(standardWait)
        schalter = input("Was soll ich tun? [Schalter betätigen/Kabelsalat analysieren/Weitersuchen]: ")
        if int(schalter) == 3:
            print("\nDer Raum ist zu dunkel, ich sehe kaum 2 Meter vor mir. Ich sollte nicht so im Dunkeln laufen")
            time.sleep(standardWait)
            print("Ich kehre zu dem Schalter zurück.")
            time.sleep(standardWait)
        elif int(schalter) == 1 and kabelsalat == False:
            os.system('cls||clear')
            death_Bild()
            print("Du hast das Haus in die Luft gejagt! GAME OVER!")
            playsound("End.mp3")
            time.sleep(endWait)
            quit()
        elif int(schalter) == 1 and kabelsalat == True:
            os.system('cls||clear')
            print("\nDie Lichter gehen an! Das ganze Haus wird mit Strom versorgt.")
            time.sleep(standardWait)
            print("Doch meine Errinerung steht immernoch im Dunkeln.")
            time.sleep(standardWait)
            print("Ich weiß weder nicht wo ich bin und wie ich hierher gekommen bin.")
            time.sleep(standardWait)
            print("Ich bin gestern, falls es gestern passiert ist, ins Bett gegangen und bin hier aufgewacht.")
            time.sleep(standardWait)
            print("Ich sollte mich aber auf das wesentliche Konzentrieren.")
            time.sleep(standardWait)
            print("Ich MUSS hier RAUS. Und am besten nachvollziehen, was passiert ist")
            time.sleep(standardWait)
            loop = False
        elif int(schalter) == 2:
            verlasse_schalter=False
            while verlasse_schalter!=True:
                os.system('cls||clear')
                print("Es sind links, verschiedene,durchnummerierte Kabeln mit bestimmten Farben zu sehen.")
                print("Rechts sind ebenfalls farbige, durchnummerierte Einsteckbüchsen zu sehen.")
                print("Einige Kabeln sind bereit verschaltet.\n")
                update_schalter()
                inp_kabel=input("\nWelchen Kabel soll ich zuerst verwalten? [Kabelnummer eingeben/beliebige Zahl, um den Schalter zu verlassen]: ")
                if int(inp_kabel)>3 or int(inp_kabel)<0:
                    verlasse_schalter=True
                    break
                else:
                    inp_buechse=input("In welche Büchse soll ich diesen Kabel stecken? [Büchsennummer eingeben/beliebige Zahl, um den Kabel durchzuschneiden]: ")
                    if int(inp_buechse)>3 or int(inp_buechse)<0:
                        verbindungen[int(inp_kabel)][1]=4
                    else:
                        verbindungen[int(inp_kabel)][1]=int(inp_buechse)
                    for i in range(0,4):
                        if verbindungen[i][1]==int(inp_buechse) and verbindungen[i][0]!=int(inp_kabel):
                            verbindungen[i][1]=4
                    if verbindungen[0] != [0,2]:
                        os.system('cls||clear')
                        print("Du hättest den roten Draht nicht durchschneiden sollen!\n")
                        time.sleep(standardWait)
                        death_Bild()
                        print("Die BOMBE IST HOCHGEGANGEN!")
                        playsound("End.mp3")
                        time.sleep(endWait)
                        quit()
            if verbindungen == loesung:
                kabelsalat = True
            else:
                kabelsalat = False