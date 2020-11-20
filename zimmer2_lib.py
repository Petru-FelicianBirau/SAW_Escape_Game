import time
import os
from colorama import Fore, Back, Style 

def keller_intro():
    print("\nIch befinde mich nun in einer Art Keller.")
    print("Die Tapete an der Wand sind zerrissen und die Wände stehen kurz vor dem Kollaps.")
    print("In den Schatten des roten, künstlichen Lichts macht sich eine massive Unordnung erkennbar.")

def keller(richtung: int):
    if richtung == 0:
        print("\nDa befindet sich dir Tür zum Arbeitszimmer.")
        print("Ansonsten gibt es in diese Richtung nichts erwähnenswertes.")
    if richtung == 1:
        print("\nDa ist eine leere Wand.")
    if richtung == 2:
        print("\nDa ist ein Tisch.")
    if richtung == 3:
        print("\nIch sehe eine Glühbirne.")

def interaktion21():
    print("Ich kann nichts tun in der Richtung.")

def interaktion22():
    print("Dort gibt es keine Interaktion.")

def interaktion23():
    print("Da kann ich nichts machen.")