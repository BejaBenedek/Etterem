import menu
import recept

raktar = []
raktarfajl = open("raktar.csv","r",encoding="utf-8")
for sor in raktarfajl:
    bemenet = sor.strip().split(";")
    raktar.append(bemenet)
raktarfajl.close()

def alapra_allitas(lista):
    kiiras = open("raktar.csv", "w", encoding="utf-8")
    i = 0
    while i < len(lista):
        kiiras.write(f"{lista[i][0]};{lista[i][1]}\n")
        i += 1

def kivonas(rendeles):
    raktar = []
    hozzavalok = recept.hozzavalok(rendeles)

    raktarfajl = open("raktar.csv", "r", encoding="utf-8")
    for sor in raktarfajl:
        raktar.append(sor.strip().split(";"))
    raktarfajl.close()

    if menu.rajtavane(rendeles):
        vaneleg = True
        i = 0
        while i < len(hozzavalok):
            z = 0
            while z < len(raktar):
                if hozzavalok[i][0] == raktar[z][0]:
                    if int(raktar[z][1]) - int(hozzavalok[i][1]) >= 0:
                        pass
                    else:
                        vaneleg = False
                        return "nincs elég hozzávaló a raktárban"
                z += 1
            i += 1
        
        if vaneleg == True:
            i = 0
            while i < len(hozzavalok):
                z = 0
                while z < len(raktar):
                    if hozzavalok[i][0] == raktar[z][0]:
                        raktar[z][1] = str(int(raktar[z][1]) - int(hozzavalok[i][1]))
                    z += 1
                i += 1
            
            kiiras = open("raktar.csv", "w", encoding="utf-8")
            i = 0
            while i < len(raktar):
                kiiras.write(f"{raktar[i][0]};{raktar[i][1]}\n")
                i += 1
            kiiras.close()