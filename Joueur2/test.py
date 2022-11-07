import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur2\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

print(data["7"]["reponse1"]["reponse"])