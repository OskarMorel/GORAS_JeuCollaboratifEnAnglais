import socket
import json

with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur1\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

# with ... as ... pas utilisable ici car socket automatiquement fermée dès la sortie du bloc !
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Description socket : ',s)
except OSError:
    print('Création socket échouée')
else:
    print('Création socket réussie')
    coord_S = ('127.0.0.1', 65432)
    try:
        s.bind(coord_S)
        s.listen(1)
    except OSError:
        print('bind() échoué')
        s.close()
        
    else:
        print('bind() réussi')
        

(s_comm, coord_C) = s.accept()
print("Client connecté\n")

question = s_comm.recv(1024)
print(question.decode() + "\n")
print(data["1"]["reponses"]["reponse1"] + "\n")
print(data["1"]["reponses"]["reponse2"] + "\n")


try:
    s_comm.close()
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')

