recepteklista = []

receptfajl = open("recept.csv","r", encoding="utf-8")
for sor in receptfajl:
    bemenet = sor.strip().split(";")
    recepteklista.append(bemenet)

def torles(receptek):
    ujreceptek = []
    
    ker = str(input("melyik receptet szeretnéd törölni? "))
    i = 0

    while i < len(receptek):
        if receptek[i][0] != ker:
            ujreceptek.append(receptek[i])
        i += 1
    
    return ujreceptek

def hozzaadas(receptek):
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
            receptek.append(hozzavalo)    
            hozzavalo = []
            i += 1
        i = 0  
        z += 1

    return receptek
