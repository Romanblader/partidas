import json

file = open(f"./habilidadesProfesionales.json", "r", encoding="UTF-8")
wFile = open(f"./listaHabilidades.txt", "w", encoding="UTF-8")

habinfo = json.loads(file.read())
habs = habinfo["profesionales"]
trans = habinfo["Equivalencias"]

for hab in habs:
    wFile.write(hab["Nombre"] + ": @{" + trans[hab["Caracteristicas"][0]] + "}+@{" + trans[hab["Caracteristicas"][1]] + "}\n")
    print(hab["Nombre"] + ": @{" + trans[hab["Caracteristicas"][0]] + "}+@{" + trans[hab["Caracteristicas"][1]] + "}")

wFile.close()