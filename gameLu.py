import time
import webbrowser

print("Hallo Mensch\n"+"Ich bin ein Programm und heiße Alex")
time.sleep(2)
print("Keine sorge ich bin zwar mit Alexa verwandt hab aber nix mit ihr zu tun;)")
time.sleep(2)
n = input("Wie heißt du: ") ##n ist der Name der Person
print("Hallo "+n)
g = input("Wie geht es dir? [ gut / schlecht ] ")##g ist die Gefühlslage
if g == "gut":
    print("Das freut mich:)")
    h = input("Hast du Humor? :) [ ja / nein ] ")
    if h == "ja":
        print("Gut dann erzähle ich dir einen Witz\n"+"Was sind acht Hobbits?")
        time.sleep(2)
        print("Na weist du es "+n)
        time.sleep(3)
        print(" Ein Hobbyte!")
        time.sleep(2)
        print("Haha ich liebe diesen Witz XD")
    elif h == "nein":
        print("schade ich wollte dir einen Witz erzählen :(") 
    else:
        print("Fehler\n"+"Ich konnte dich nicht verstehen"+n)
elif g == "schlecht":
    print("Das ist schade :'(\n"+"Morgen gehts dir hoffentlich wieder besser\n"+n+" Hier ist etwas um dich aufzuheitern ;)")
    time.sleep(3)
    webbrowser.open('https://www.youtube.com/watch?v=c24EJgd_yhQ')
    time.sleep(5)
    print("Katzen sind doch was herrliches :)\n"+"Die sind so süß :)")
    c = input("Findest du nicht auch "+n+"? [ ich liebe Katzen / igitt diese Flohsäcke] ")
    if c == "ich liebe Katzen":
        print("Freut mich sehr "+n+"\nich hoffe dir geht es nach dem Video etwas besser :)")
    elif c == "igitt diese Flohsäcke":
        print("schade ich dachte, dass ich dich aufheitern kann:'(")   
    else:
        print("Du hast keine meinung dazu? "+n+"\nSchade:/")
else:
    print("Tut mir leid \n"+"Ich bin leider nur ein Programm und konnte dich nicht verstehen :(")
    f = input("hast du dich vertippt? [ ja leider / nein ich wollte dich pranken] ")
    if f == "ja leider":
        print("ok das ist nicht schlimm :)\n"+"Oh ich bin schon so lange wach?")
    elif f == "nein ich wollte dich pranken":
        print("Soso "+n+" du hast mich erfolgreich geprankt, dass kann ich aber auch;)")
        time.sleep(3)
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    else:
        print("Oje du hast dich also schon wieder vertippt :/")
time.sleep(3)
print("Ich muss jetzt leider los\n"+"Es hat mich gefreut dich kennen zu lernen:) "+n+"\nich wünsche dir noch einen schönen Tag :)")
