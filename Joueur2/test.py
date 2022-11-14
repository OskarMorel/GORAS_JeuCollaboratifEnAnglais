import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\sae\jeuCollabTest\Joueur2\QA.json') as mon_fichier:
    data = json.load(mon_fichier)


i = "0"
j = 1
ok = True
i = str(j)
while ok:

    if data["1"]["reponse1"]["cleNext"] == "2":
        print(data[i]["reponse1"]["reponse"])
        ok = False
    elif data[i]["reponse2"]["cleNext"] == "3":
        print(data[i]["reponse2"]["reponse"])
        ok = False

