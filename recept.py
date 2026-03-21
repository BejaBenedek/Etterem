def torles():
    ujreceptek = []
    
    recepteklista = []

    receptfajl = open("recept.csv","r", encoding="utf-8")
    for sor in receptfajl:
        bemenet = sor.strip().split(";")
        recepteklista.append(bemenet)
    receptfajl.close()
    ker = str(input("melyik receptet szeretnéd törölni? "))
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
    recepteklista = []

    receptfajl = open("recept.csv","r", encoding="utf-8")
    for sor in receptfajl:
        bemenet = sor.strip().split(";")
        recepteklista.append(bemenet)
    receptfajl.close()
    hozzavalo = []

    nev = str(input("mi a recept neve? "))
    hozzavalok = int(input("hány hozzávaló kell a recepthez? "))
    i = 0
    z = 0

    while z < hozzavalok:
        while i < 1:
            a = str(input("milyen hozzávaló kell? "))
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
