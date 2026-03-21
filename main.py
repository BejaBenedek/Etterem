import menu
import recept
import raktar
import vasarlok
import lezart_rendeles
import os

class asztal:
    def __init__(self,neve, rendelesek_szama, teljes_osszeg):
        self.neve = neve
        self.rendelesek_szama = rendelesek_szama
        self.teljes_osszeg = teljes_osszeg
    
    def __str__(self):
        return f"{self.neve}, {self.rendelesek_szama}, {self.teljes_osszeg}"

osszesasztal = []

asztalok_szama = 12
tobbasztal = input("lesz több asztal? ")

if tobbasztal == "igen":
    plusz = int(input("hány új asztal lesz? "))
    asztalok_szama += plusz

print(asztalok_szama, "asztal van")

i = 0
while i < asztalok_szama:
    nev = "asztal " + str(i+1)
    osszesasztal.append(asztal(nev, 0, 0))
    i += 1

os.system("cls")

