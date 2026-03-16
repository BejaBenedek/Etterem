vasarlok = []

vasarlofajl = open("raktar.csv","r",encoding="utf-8")
for sor in vasarlofajl:
    bemenet = sor.strip().split(";")
    vasarlok.append(bemenet)