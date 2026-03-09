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
