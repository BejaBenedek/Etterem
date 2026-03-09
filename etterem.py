receptek = []
menu = []
raktar = []
vasarlok = []
i = 0
menufajl = open("menu.csv","r",encoding="utf-8")
for sor in menufajl:
    bemenet = sor.strip().split(";")
    menu.append(bemenet)

receptfajl = open("recept.csv","r", encoding="utf-8")
for sor in receptfajl:
    bemenet = sor.strip().split(";")
    receptek.append(bemenet)

raktarfajl = open("raktar.csv","r",encoding="utf-8")
for sor in raktarfajl:
    bemenet = sor.strip().split(";")
    raktar.append(bemenet)

vasarlofajl = open("raktar.csv","r",encoding="utf-8")
for sor in vasarlofajl:
    bemenet = sor.strip().split(";")
    raktar.append(bemenet)
    
with open("recept.csv", "w", encoding="utf-8") as blahafajl:                                                                                                                                                    #niga
    blahafajl.write(input("recept: "))
