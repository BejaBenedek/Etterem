import menu
import recept
import raktar
import vasarlok
import lezart_rendeles
import os
import msvcrt

class asztal:
    def __init__(self, neve):
        self.neve = neve
        self.rendelesek_szama = 0
        self.teljes_osszeg = 0

    def __str__(self):
        return f"{self.neve} | {self.rendelesek_szama} db | {self.teljes_osszeg} Ft"


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
    osszesasztal.append(asztal(nev))
    i += 1

i = 0
a = 0
asztalnal = False
megy = True
while megy:
    os.system("cls")
    print("================")
    print("válassz asztalt")
    print("================")
    i = 0
    while i < len(osszesasztal):
        if i != a:
            print(f"   {osszesasztal[i].neve}")
        else:
            print(f"\033[92m\033[1m > {osszesasztal[i].neve} < \033[0m")
        i += 1
    gomb = msvcrt.getch()
    if gomb == b'w':
        a -= 1
    elif gomb == b's':
        a += 1
    if a < 0:
        a = len(osszesasztal) - 1
    elif a >= len(osszesasztal):
        a = 0
    if gomb == b'd':
        os.system("cls")
        megy = False
        mostani_asztalindex = a
        asztalnal = True


a = 0
lehetosegek = ["rendelni", "fizetni", "megtudni a felszolgálómat"]
while asztalnal == True:
    os.system("cls")
    i = 0
    print("======================")
    print("mit szeretnél csinálni")
    print("======================")
    while i < len(lehetosegek):
        if i != a:
            print(f"   {lehetosegek[i]}")
        else:
            print(f"\033[92m\033[1m > {lehetosegek[i]} < \033[0m")
        i += 1
    gomb = msvcrt.getch()
    if gomb == b'w':
        a -= 1
    elif gomb == b's':
        a += 1
    if a < 0:
        a = len(lehetosegek) - 1
    elif a >= len(lehetosegek):
        a = 0
    