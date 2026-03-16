receptek = []

receptfajl = open("recept.csv","r", encoding="utf-8")
for sor in receptfajl:
    bemenet = sor.strip().split(";")
    receptek.append(bemenet)