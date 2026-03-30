import random

def ujvasarlo():
    """ezzel az eljárással lehet új vásárlót fogadni"""
    vasarlok = []
    pincerek = []
    alapvasarlok = []
    vasarlofajl = open("vasarlok.csv","r",encoding="utf-8")
    for sor in vasarlofajl:
        bemenet = sor.strip().split(";")
        if len(bemenet) > 2:
            alapvasarlok.append(bemenet)
        else:
            vasarlok.append(bemenet)
        pincerek.append(bemenet[1])
    vasarlofajl.close()

    ideigvasarlo = []
    nev = input("Milyen névre foglalt? ")
    ideigvasarlo.append(nev)
    ideigvasarlo.append(random.choice(pincerek))
    vasarlok.append(ideigvasarlo)
    ideigvasarlo = []

    kiiras = open("vasarlok.csv","w",encoding="utf-8")
    i = 0
    while i < len(alapvasarlok):
        kiiras.write(f"{alapvasarlok[i][0]};{alapvasarlok[i][1]};{alapvasarlok[i][2]};{alapvasarlok[i][3]};{alapvasarlok[i][4]}\n")
        i += 1
    i = 0
    while i < len(vasarlok):
        kiiras.write(f"{vasarlok[i][0]};{vasarlok[i][1]}\n")
        i += 1

def osszes_vasarlo():
    """ez a függvény beolvassa és visszaadja az összes vásárlót"""
    vasarlok = []
    vasarlofajl = open("vasarlok.csv", "r", encoding="utf-8")
    for sor in vasarlofajl:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        pincer = adatok[1]
        if len(adatok) > 2:
            osszeg = int(adatok[2])
        else:
            osszeg = 0

        vasarlok.append({"nev": nev, "pincer": pincer, "osszeg": osszeg})

    vasarlofajl.close()
    return vasarlok

def rendeles_mentese(vasarlo_nev, rendeles, ar):
    """ez az eljárás elmenti a vasarlok.csv fájlba a vásárló új rendelését"""
    vasarlok = []

    vasarlofajl = open("vasarlok.csv", "r", encoding="utf-8")
    for sor in vasarlofajl:
        vasarlok.append(sor.strip().split(";"))
    vasarlofajl.close()

    for sor in vasarlok:
        if sor[0] == vasarlo_nev:
            if len(sor) > 2:
                sor[2] = str(int(sor[2]) + ar)
            else:
                sor.append(str(ar))

            sor.append(rendeles)

            rendeles_lista = sor[3:]

            darabok = {}
            for item in rendeles_lista:
                if item in darabok:
                    darabok[item] += 1
                else:
                    darabok[item] = 1

            uj_lista = []
            for nev, db in darabok.items():
                if db > 1:
                    uj_lista.append(f"{db}x {nev}")
                else:
                    uj_lista.append(nev)

            sor[:] = sor[:3] + uj_lista

    kiiras = open("vasarlok.csv", "w", encoding="utf-8")
    for sor in vasarlok:
        kiiras.write(";".join(sor) + "\n")
    kiiras.close()

def mai_profit():
    """ez a függvény kiírja hogy mennyi pénzt keresett ma az étterem"""
    vasarlok = []

    vasarlofajl = open("vasarlok.csv", "r", encoding="utf-8")
    for sor in vasarlofajl:
        vasarlok.append(sor.strip().split(";"))
    vasarlofajl.close()

    osszeg = 0

    for sor in vasarlok:
        if len(sor) > 2:
            osszeg += int(sor[2])

    return f"{osszeg} FT"