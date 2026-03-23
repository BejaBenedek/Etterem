def arazas(elelmiszer):
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