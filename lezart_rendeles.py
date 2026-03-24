def fizetes(vasarlo_neve):
    vasarlok = []

    with open("vasarlok.csv", "r", encoding="utf-8") as vasarlofajl:
        for sor in vasarlofajl:
            vasarlok.append(sor.strip().split(";"))

    fizetendo = 0

    fajlbairas = open("lezart_rendeles.csv", "a", encoding="utf-8")
    kiiras = open("vasarlok.csv", "w", encoding="utf-8")

    i = 0
    while i < len(vasarlok):
        if vasarlok[i][0] == vasarlo_neve:
            fajlbairas.write(";".join(vasarlok[i]) + "\n")
            fizetendo = int(vasarlok[i][2])
        else:
            kiiras.write(";".join(vasarlok[i]) + "\n")
        i += 1

    fajlbairas.close()
    kiiras.close()

    return fizetendo

def kiiras():
    fajl = open("lezart_rendeles.csv", "r", encoding="utf-8")

    for sor in fajl:
        adatok = sor.strip().split(";")
        nev = adatok[0]
        pincer = adatok[1]
        osszeg = adatok[2]
        rendelesek = adatok[3:]

        print(f"Vásárló: {nev}")
        print(f"Pincér: {pincer}")
        print(f"Fizetett: {osszeg} Ft")
        print("Rendelések:")

        for r in rendelesek:
            print(f" - {r}")

        print("--------------------------")

    fajl.close()