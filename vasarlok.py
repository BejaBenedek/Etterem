import random
vasarlok = []
pincerek = []

vasarlofajl = open("vasarlok.csv","r",encoding="utf-8")
for sor in vasarlofajl:
    bemenet = sor.strip().split(";")
    pincerek.append(bemenet[1])

jon = True
while jon:
    ujvendeg = input("Jött új vendég?")
    if ujvendeg =="igen":
        nev = input("Milyen névre foglalt")
        vasarlok.append(nev)
        vasarlok.append(random.choice(pincerek))
    if ujvendeg == "nem":
        jon = False

print(vasarlok)
