import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
<<<<<<< HEAD
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

=======
with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur2\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

print(data["7"]["reponse1"]["reponse"])
>>>>>>> db69712edc2fe0ebcc7a51b5514eb223db207feb
