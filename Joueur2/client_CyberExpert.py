import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur2\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

# Création de la socket du client
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Description socket : ', s)
except OSError:
    print('Création socket échouée')
else:
    print('Création socket réussie')
    coord_S = ('127.0.0.1', 65432)

# Connection au serveur (Le DSI)
s.connect(coord_S)
print("Connection effectuée")

# Envoi de la première question au serveur (DSI)
question = data["1"]["question"] + "\n**********************************************************"
print("1ère question envoyée : " + question)
s.send(question.encode())

# Réception de la réponse envoyée par le serveur (DSI)
question = s.recv(1024)
if question == 2:
    print("The answer is : " + data["1"]["reponse1"]["reponse"])
    cleSuivante = data["1"]["reponse1"]["cleNext"]
else:
    print("The answer is : " + data["1"]["reponse2"]["reponse"])
    cleSuivante = data["1"]["reponse2"]["cleNext"]

#TODO Faire la boucle pour les questions
finJeu = False
choixValide = False
while finJeu == False:
    while choixValide == False:
        print("1 : " + data[cleSuivante]["question1"]["question"])
        # Verifie que la clé existe
        if data[cleSuivante]["question2"]["question"] :
            print("2 : " + data[cleSuivante]["question2"]["question"])
        question = input("Choose between 1 and 2 : ")
        if question == "1":
            choixValide = True
            cleSuivante = data[cleSuivante]["question1"]["cleNext"]
        elif question == "2":
            choixValide = True
            cleSuivante = data[cleSuivante]["question2"]["cleNext"]
        else:
            choixValide = False

    s.send(cleSuivante.encode())
    question = s.recv(1024)

    if question == 2:
        print("The answer is : " + data[cleSuivante]["reponse1"]["reponse"])
        cleSuivante = data[cleSuivante]["reponse1"]["cleNext"]
        if cleSuivante == 0:
            finJeu = True
    elif question == 1:
        print("The answer is : " + data[cleSuivante]["reponse2"]["reponse"])
        cleSuivante = data[cleSuivante]["reponse2"]["cleNext"]
        if cleSuivante == 0:
            finJeu = True



# Fermeture de la socket
try:
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')