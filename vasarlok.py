import random

def ujvasarlo():
    vasarlok = []
    pincerek = []
    alapvasarlok = []
    vasarlofajl = open("vasarlok.csv","r",encoding="utf-8")
    for sor in vasarlofajl:
        bemenet = sor.strip().split(";")
        if len(bemenet) > 2:
            alapvasarlok.append(bemenet)
        else:
            vasarlok.append(bemenet)
        pincerek.append(bemenet[1])
    vasarlofajl.close()

    ideigvasarlo = []
    nev = input("Milyen névre foglalt")
    ideigvasarlo.append(nev)
    ideigvasarlo.append(random.choice(pincerek))
    vasarlok.append(ideigvasarlo)
    ideigvasarlo = []

    kiiras = open("vasarlok.csv","w",encoding="utf-8")
    i = 0
    while i < len(alapvasarlok):
        kiiras.write(f"{alapvasarlok[i][0]};{alapvasarlok[i][1]};{alapvasarlok[i][2]};{alapvasarlok[i][3]};{alapvasarlok[i][4]}\n")
        i += 1
    i = 0
    while i < len(vasarlok):
        kiiras.write(f"{vasarlok[i][0]};{vasarlok[i][1]}\n")
        i += 1
