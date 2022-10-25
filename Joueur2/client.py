import socket
import json

with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur1\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Description socket : ',s)
except OSError:
    print('Création socket échouée')
else:
    print('Création socket réussie')
    coord_S = ('127.0.0.1', 65432)


s.connect(coord_S)
print("Connection effectuée") 

question = data["1"]["question"] + "\n**********************************************************"
s.send(question.encode()) 


try:
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')