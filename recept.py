import os
import menu

def torles():
    """kitöröl a receptek közül és a menüről egy bekért ételt"""
    ujreceptek = []
    
    recepteklista = []

    receptfajl = open("recept.csv","r", encoding="utf-8")
    for sor in receptfajl:
        bemenet = sor.strip().split(";")
        recepteklista.append(bemenet)
    receptfajl.close()
    ker = str(input("melyik receptet szeretnéd törölni? "))
    menu.menutorles(ker)
    i = 0

    while i < len(recepteklista):
        if recepteklista[i][0] != ker:
            ujreceptek.append(recepteklista[i])
        i += 1
    
    receptkiiras = open("recept.csv", "w", encoding="utf-8")
    i = 0
    while i < len(ujreceptek):
        receptkiiras.write(f"{ujreceptek[i][0]};{ujreceptek[i][1]};{ujreceptek[i][2]}\n")
        i += 1
    receptkiiras.close()

def hozzaadas():
    """hozzáad egy tetszőleges receptet a recptek közé és a menühöz"""
    recepteklista = []

    receptfajl = open("recept.csv","r", encoding="utf-8")
    for sor in receptfajl:
        bemenet = sor.strip().split(";")
        recepteklista.append(bemenet)
    receptfajl.close()
    hozzavalo = []
    os.system("cls")
    nev = str(input("mi a recept neve? "))
    menu.arazas(nev)
    os.system("cls")
    hozzavalok = int(input("hány hozzávaló kell a recepthez? "))
    i = 0
    z = 0

    while z < hozzavalok:
        while i < 1:
            os.system("cls")
            a = str(input("milyen hozzávaló kell? "))
            os.system("cls")
            b = int(input("hány darab kell? "))
            hozzavalo.append(nev)
            hozzavalo.append(a)
            hozzavalo.append(b)
            recepteklista.append(hozzavalo)    
            hozzavalo = []
            i += 1
        i = 0  
        z += 1

    receptkiiras = open("recept.csv", "w", encoding="utf-8")
    i = 0
    while i < len(recepteklista):
        receptkiiras.write(f"{recepteklista[i][0]};{recepteklista[i][1]};{recepteklista[i][2]}\n")
        i += 1
    receptkiiras.close()


def hozzavalok(rendeles):
    """visszadaja az összes recept hozzávalóját"""
    recepteklista = []

    receptfajl = open("recept.csv", "r", encoding="utf-8")
    for sor in receptfajl:
        recepteklista.append(sor.strip().split(";"))

    hozzavalok_lista = []
    i = 0
    
    while i < len(recepteklista):
        if recepteklista[i][0] == rendeles:
            ideiglenes = []
            ideiglenes.append(recepteklista[i][1])
            ideiglenes.append(recepteklista[i][2])
            hozzavalok_lista.append(ideiglenes)
        i += 1

    return hozzavalok_lista

def recept_kiirasa(recept):
    """kiírj egy tetszőleges receptet"""
    recepteklista = []

    receptfajl = open("recept.csv", "r", encoding="utf-8")
    for sor in receptfajl:
        recepteklista.append(sor.strip().split(";"))
    receptfajl.close()

    kiiras = f"Recept: {recept}\n"
    kiiras += "Hozzávalók:\n"

    for sor in recepteklista:
        if sor[0] == recept:
            hozzavalo = sor[1]
            mennyiseg = sor[2]
            kiiras += f"- {hozzavalo}: {mennyiseg}\n"

    return kiiras


def osszes_recept_kiirasa():
    """kiírja az összes receptet"""
    receptek = []

    f = open("recept.csv", "r", encoding="utf-8")
    for sor in f:
        receptek.append(sor.strip().split(";"))
    f.close()

    kiiras = ""
    aktualis_recept = ""

    for sor in receptek:
        if len(sor) >= 3:
            recept_nev = sor[0]
            hozzavalo = sor[1]
            mennyiseg = sor[2]

            if recept_nev != aktualis_recept:
                aktualis_recept = recept_nev
                kiiras += f"\nRecept: {recept_nev}\nHozzávalók:\n"

            kiiras += f"- {hozzavalo}: {mennyiseg}\n"

    return kiiras