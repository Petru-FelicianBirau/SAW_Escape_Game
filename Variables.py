from colorama import Fore, Back, Style

##Setup:
endWait = 5
standardWait = 2
loop = True

##Main:
verfügbare_Zimmer = ["Arbeitszimmer", "None", "None"]
zimmer = 0
richtung = 0

#Zimmer_0:
vl = [["Stieglitz, Thomas","Universität Freiburg\nInstitut für Mikrosystemtechnik - IMTEK\nProfessur für Biomedizinische Mikrotechnik\nVermisst seit: 14. Februar 2019"],["Prof. Dr. Oliver Paul","Universität Freiburg\nInstitut für Mikrosystemtechnik - IMTEK\nProfessur für Materialien der Mikrosystemtechnik\nVermisst seit: 22. Februar 2019"],["Prof. Dr. Norbert Südkamp","Universität Freiburg\nMedizinische Fakultät\nDekan der Medizinischen Fakultät\nVermisst seit: 03. März 2019"]]
za = [["Professoren an der Uni Freiburg misteriöserweise verschwunden","24. Februar 2019\n\nEs ist ein schlechtes Jahr an der Universität Freiburg. \nMehrere Studenten können ihre Module nicht weiterführen, denn die Professoren verschwinden spurlos.\nDie Ermittlungen der Polizei sind am Laufen, jedoch bekommt die Öffentlichkeit noch keinerlei Informationen.\nEs wird davon ausgegangen, dass diese vom gleichen Täter entführt wurden..."],
    ["Supraleiter des Fraunhoferinstituts und moderne Austattung der Technischen Fakultät gestohlen","17. März 2019\n\nDie Lage im Lernzentzum Freiburg ist sehr umstritten.\nMehrere Vorfällle in der Universität Freiburg und Forschungsabteilungen fördern viele Lerninstitute in Stillstand.\nGestern wurde in den Fraunhofer Institut und Technische Fakultät eingebrochen.\nDabei wurden Türen gesprengt und Austattung gestohlen.\nEs wird auf Veröffentlichungen der Polizei bezüglich weiterer Ermittlungen gewartet.\nSeit Monate sind jegliche Äußerungen der Polizei Fehlanzeige..."],
    ["Freiburg als Universitätszentrum","14. Juli 2019\n\nSeit zwei Monaten hat sich die Lage an der Universität Freiburg verbessert.\nDas Studierendeleben wurde wieder aufgenommen und neue Professoren starten ihre Karriere.\nDie Ermittlungen der Entführungen und gestohlenen Ausstattungen laufen dagegen nicht.\nDie Öffentlichkeit wartet darauf neue Informationen und Aufklärungen zu bekommen.\nDie Angehörige der Vermissten erleben einen schlimmen Alptraum..."]]
buch_t = ["TITAN-4 von Frederik Pohl","Honor Harrington 17. Um jeden Preis von David Weber","Die Genesis-Affäre: Mind Control von Martin de Wolf"]
buch_i = ["»Du kannst mich totschlagen…« Cooley fühlt(E) sich verwirrt; willenlos schritt er vorwärts und schwang seinen Stab. Sie näherten sich der Mauer. Als sie nur noch wenige Schritte davon entfernt waren, sprang plötzlich ein Hase aus seiner Deckung. Er hoppelte in diese Richtung, dann in die andere, strengte se(I)ne Hinterläufe gewaltig an. Von der hera(N)marschierenden Reihe völlig in Bestürzung versetzt, jagte er auf die Bresche zwischen Baker und Cooley zu. »Vorsicht!« schrie Cooley unwillkürlich. Bakers Stab schwang unmittelbar über den Hasen hinweg. Nichts geschah. Der Hase hoppelte davon. Cooley und ein paar andere drehten (S)ich um und schauten ihm nach. Er überquerte die dunkle Fläche und verschwand dahinter im hohen Gras.","Unmittelbar vor der Hyp(E)rgrenze überquerten die großen LAC-Träger der Aviary -Klasse und ihr Geleitschutz aus Schlachtkreuzern d(I)e Alpha-Mauer und kehrten in den Normalraum zurück. Im Verband waren nur drei der superdread(N)oughtgroßen Schiffe, doch ihre Hangars spien beinahe sechshundert Leichte Angriffsboote aus. Die havenitischen LACs der Cimeterre -Klasse mochten eine leichtere Bewaffnung tragen als die Shrikes und Ferret(S) des Sternenkönigreichs von Manticore, ihnen in jeder Hinsicht unterlegen sein und eine kürzere Reichweite haben, doch ihrer augenblicklichen Aufgabe waren sie mehr als gewachsen.Während sie auf Vektoren systemeinwärts beschleunigten, die zur industriellen Infrastruktur von Alizon führten, entdeckten sie, dass sie unerwartetes Glück hatten: zwei schwerfällige Frachter, die beide manticoranische Kennungen abstrahlten und annähernd dem gleichen Kurs folgten, fanden sich genau im Anlaufweg des Kampfverbandes wieder; bereits jetzt waren sie in äußerster Raketenschussweite.","»Hey – Ruschkow«, rief er, »was hast du als Nächstes vor? Willst du das gan(Z)e Europa-Center in die Luft sprengen? Aber du bist schlau genug und weißt genau, dass dies niemand riskieren würde. Du hast ge(W)onnen – Ruschkow.« Talert ließ sich nicht anmerken, dass er vom Gegenteil überzeugt war. »Lass wenigstens die Kellnerin laufen. Sie hat mit alledem nichts zu tun. Du wolltest mich – du hast mich. Du wolltest die Regierung erpr(E)ssen und hast es getan. Was willst du noch? Ab jetzt ist es nur noch eine Sache zwischen dir und mir. Also, lass die Frau gehen und dann kannst du mit m(I)r abrechnen.«. Ruschkow schob sein Notebook etwas von sich weg und sah Talert mit zusammengekniffenen Augen an, der diesen Gesichtsausdruck an Ruschkow abgrundtief hasste. »Ich habe dich schon damals unterschätzt«, sagte Ruschkow nach einem kurzen Moment, »du warst clever und bist es heute immer noch. Wenn ich darüber nachdenke, dann hast du recht. Das Mädchen nützt mir wirklich nichts.«"]
code = [0,0,0,0,0,0,0]
code_lsg = [1,1,2,3,5,8,13]

#Quest_Open_Z1:
status_led = [Fore.RED,Fore.RED,Fore.RED]
bild = [1,3,2]
led = [0,0,0]
tur_offen = False

def is_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False