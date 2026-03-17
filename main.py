import menu
import recept
import raktar
import vasarlok
import lezart_rendeles
import os

class asztal:
    def __init__(self, ):
        

osszesasztal = []

asztalok_szama = 12
tobbasztal = str(input("lesz több asztal? "))

if tobbasztal == "igen":
    plusz = int(input("hány új asztal lesz? "))
    asztalok_szama += plusz
else:
    asztalok_szama += 0

print(asztalok_szama, "asztal van")


while len(osszesasztal) < asztalok_szama:
    osszesasztal.append()

