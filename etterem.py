receptek = []
menu = []
raktar = []
vasarlok = []
i = 0
menufajl = open("menu.csv","r",encoding="utf-8")
for sor in menufajl:
    bemenet = sor.strip().split(";")
    menu.append(bemenet)

print(menu)