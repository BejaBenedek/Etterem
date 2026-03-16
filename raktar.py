raktar = []

raktarfajl = open("raktar.csv","r",encoding="utf-8")
for sor in raktarfajl:
    bemenet = sor.strip().split(";")
    raktar.append(bemenet)