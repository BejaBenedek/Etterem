def arazas(elelmiszer):
    """új termék hozzáadásakor ezzel árazuk a terméket, a paraméter az étel neve"""
    menu = []

    menufajl = open("menu.csv","r",encoding="utf-8")
    for sor in menufajl:
        bemenet = sor.strip().split(";")
        menu.append(bemenet)
    menufajl.close()
    menun = []
    ar = int(input("mennyibe kerülne az új étel/ital? "))
    menun.append(elelmiszer)
    menun.append(ar)
    menu.append(menun)
    menun = []

    kiiras = open("menu.csv","w",encoding="utf-8")
    i = 0
    while i < len(menu):
        kiiras.write(f"{menu[i][0]};{menu[i][1]}\n")
        i += 1

def menutorles(nev):
    """az admin módban egy recept törlésénél ezt használjuk, hogy a menüről is levegye az ételt, a paraméter az eltávolítandó étel"""
    menu = []
    ujmenu = []

    menufajl = open("menu.csv","r",encoding="utf-8")
    for sor in menufajl:
        bemenet = sor.strip().split(";")
        menu.append(bemenet)
    menufajl.close()

    i = 0
    while i < len(menu):
        if menu[i][0] != nev:
            ujmenu.append(menu[i])
        i += 1
    
    kiiras = open("menu.csv","w",encoding="utf-8")
    i = 0
    while i < len(ujmenu):
        kiiras.write(f"{ujmenu[i][0]};{ujmenu[i][1]}\n")
        i += 1

def menukiiras():
    """amikor egy asztalnál kérik a menüt, ezzel írjuk ki"""
    menu = []

    menufajl = open("menu.csv","r",encoding="utf-8")
    for sor in menufajl:
        bemenet = sor.strip().split(";")
        menu.append(bemenet)
    menufajl.close()

    i = 0
    while i < len(menu):
        print(f"{menu[i][0]} | {menu[i][1]} FT")
        i += 1

def rajtavane(rendeles):
    """ez a függvény megnézi, hogy a paraméterben lévő rendelés rajtavan-e a menün"""
    menu = []

    menufajl = open("menu.csv","r",encoding="utf-8")
    for sor in menufajl:
        bemenet = sor.strip().split(";")
        menu.append(bemenet)
    menufajl.close()

    i = 0
    igen = False #eldöntés

    while i < len(menu):
        if menu[i][0] == rendeles:
            igen = True
        i += 1
    
    return igen

def ar(rendeles):
    """visszaadja a paraméterben való rendelés árát"""
    menu = []

    menufajl = open("menu.csv","r",encoding="utf-8")
    for sor in menufajl:
        bemenet = sor.strip().split(";")
        menu.append(bemenet)
    menufajl.close()
    
    i = 0

    while i < len(menu):
        if menu[i][0] == rendeles: #kiválasztás
            ar = int(menu[i][1])
        i += 1
    
    return ar