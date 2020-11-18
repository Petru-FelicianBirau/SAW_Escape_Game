from tutorial import tutorial
from intro import intro
import time
import os
from colorama import Fore, Back, Style 

inp_tutorial=input("Tutorial überspringen? [1: Nein / Beliebige Nummer: Überspringen / Beliebige Taste: Schliessen] :" )
if int(inp_tutorial)==1:
    tutorial()
intro()
os.system('cls||clear')