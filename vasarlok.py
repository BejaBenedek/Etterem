vasarlok = []
pincerek = []

vasarlofajl = open("vasarlok.csv","r",encoding="utf-8")
for sor in vasarlofajl:
    bemenet = sor.strip().split(";")
    vasarlok.append(bemenet)
    pincerek.append(bemenet[1])

