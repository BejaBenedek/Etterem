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
        self.vasarlo_neve = ""

    def __str__(self):
        return f"{self.neve} | {self.rendelesek_szama} db | {self.teljes_osszeg} Ft | vásárló: {self.vasarlo_neve}"

class menupont:
    def __init__(self, neve):
        self.neve = neve
    def __str__(self):
        return f"{self.neve}"

osszesasztal = []

asztalok_szama = 12
tobbasztal = input("lesz több asztal? ")

if tobbasztal == "igen":
    plusz = int(input("hány új asztal lesz? "))
    asztalok_szama += plusz

print(asztalok_szama, "asztal van")

vasarlok_lista = vasarlok.osszes_vasarlo()

i = 0
while i < asztalok_szama:
    nev = "asztal " + str(i+1)
    uj_asztal = asztal(nev)
    if i < len(vasarlok_lista):
        uj_asztal.vasarlo_neve = vasarlok_lista[i]
    osszesasztal.append(uj_asztal)
    i += 1

osszesasztal.append(menupont("admin"))
osszesasztal.append(menupont("új vásárló fogadása"))

i = 0
a = 0
asztalnal = False
megy = True
kileptele = False
admin = False
while kileptele == False:
    while megy:
        os.system("cls")
        print("=====================================================")
        print("válassz asztalt (w/s, d a kilépés, enter a választás)")
        print("=====================================================")
        i = 0
        while i < len(osszesasztal):
            if i != a:
                print(f"   {osszesasztal[i].neve}")
            if i == a:
                print(f"\033[92m\033[1m > {osszesasztal[i].neve} < \033[0m")
            i += 1

        gomb = msvcrt.getch()
        if gomb == b'w':
            a -= 1
        elif gomb == b's':
            a += 1
        if a < 0:
            a = len(osszesasztal)-1
        elif a >= len(osszesasztal):
            a = 0
        if gomb == b'\r' and osszesasztal[a].neve != "admin" and osszesasztal[a].neve != "új vásárló fogadása":
            os.system("cls")
            megy = False
            mostani_asztalindex = a  ########fontos
            asztalnal = True
        if gomb == b'\r' and osszesasztal[a].neve == "admin":
            os.system("cls")
            megy = False
            admin = True
        if gomb == b'd':
            os.system("cls")
            megy = False
            kileptele = True
            print("vége")
        if gomb == b'\r' and osszesasztal[a].neve == "új vásárló fogadása":
            os.system("cls")
            megy = False
            if len(vasarlok_lista) < asztalok_szama:
                vasarlok.ujvasarlo()
                vasarlok_lista = vasarlok.osszes_vasarlo()
            uj_vasarlo = vasarlok_lista[-1]

            for asztal_obj in osszesasztal:
                if isinstance(asztal_obj, asztal) and asztal_obj.vasarlo_neve == "":
                    asztal_obj.vasarlo_neve = uj_vasarlo
                    break
                megy = True
            else:
                print("sajnos megtelt az étterem")
                gomb = msvcrt.getch()
                if gomb == b'd':
                    megy = True
            

    a = 0
    lehetosegek = ["rendelni", "fizetni", "megtudni a felszolgálómat", "menüt kérek"]
    while asztalnal == True:
        os.system("cls")
        i = 0
        if osszesasztal[mostani_asztalindex].vasarlo_neve != "":
            print("=================================")
            print(f"mit szeretnél csinálni({osszesasztal[mostani_asztalindex].neve})")
            print("=================================")
            print(f"vásárló neve: {osszesasztal[mostani_asztalindex].vasarlo_neve}")
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
            if gomb == b'd':
                asztalnal = False
                megy = True

            menutnez = False
            if gomb == b'\r' and lehetosegek[a] == "menüt kérek":
                asztalnal = False
                menutnez = True
                os.system("cls")
                menu.menukiiras()
                gomb = msvcrt.getch()
                if gomb == b'd':
                    os.system("cls")
                    asztalnal = True
        if osszesasztal[mostani_asztalindex].vasarlo_neve == "":
            print("=================" )
            print("Ez az asztal üres")
            print("=================")

            gomb = msvcrt.getch()
            if gomb == b'd':
                asztalnal = False
                megy = True
                

    a = 0
    lehetosegek = ["recept hozzáadása", "recept törlése", "raktár",]
    while admin == True:
        os.system("cls")
        i = 0
        print("=================================")
        print("mit szeretnél csinálni(admin mód)")
        print("=================================")
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
        if gomb == b'd':
            admin = False
            megy = True
        if gomb == b'\r' and lehetosegek[a] == "recept hozzáadása":
            os.system("cls")
            recept.hozzaadas()
        if gomb == b'\r' and lehetosegek[a] == "recept törlése":
            os.system("cls")
            recept.torles()