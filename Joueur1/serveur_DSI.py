import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur1\QA.json') as QA:
    data = json.load(QA)

# Création de la socket du serveur
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Description socket : ', s)
except OSError:
    print('Création socket échouée')
else:
    print('Création socket réussie')
    coord_S = ('127.0.0.1', 65432)
    # Association des coordonnées à la socket créée 
    try:
        s.bind(coord_S)
        s.listen(1)
    except OSError:
        print('bind() échoué')
        s.close()
    else:
        print('bind() réussi')

# Acceptation de la connexion avec le client (l'expert en cybersécurité)
(s_comm, coord_C) = s.accept()
print("The Cybersecurity expert is ready talk with you !!\n")

# Réception de la première question envoyée par le client (l'expert en cybersécurité)
question = s_comm.recv(1024)
print("Question : " + question.decode())
print("\n***************************************")

# Choix de la réponse à envoyer au client (l'expert en cybersécurité)
ok = False
while ok == False:
    print("1 : " + data["1"]["reponse1"]["reponse"])
    print("2 : " + data["1"]["reponse2"]["reponse"])
    answer = input("Choose between 1 and 2 : ")
    if answer == "1":
        ok = True
        cleSuivante = data["1"]["reponse1"]["cleNext"]
    elif answer == "2":
        ok = True
        cleSuivante = data["1"]["reponse2"]["cleNext"]
    else:
        ok = False

# Envoi de la réponse choisie
print(answer)
s_comm.send(answer.encode())

#TODO Faire la boucle pour les réponses
finJeu = False
choixValide = False
while finJeu == False:
    cleQuestion = s_comm.recv(1024)
    print(cleQuestion.decode())
    print("Question : " + question.decode())
    print("\n***************************************")
    
    while choixValide == False:
        print("1 : " + data[str(cleQuestion)]["reponse1"]["reponse"])
        print("2 : " + data[str(cleQuestion)]["reponse2"]["reponse"])
        answer = input("Choose between 1 and 2 : ")
        if answer == "1":
            choixValide = True
            cleSuivante = data[cleSuivante]["reponse1"]["cleNext"]
        elif answer == "2":
            choixValide = True
            cleSuivante = data[cleSuivante]["reponse2"]["cleNext"]
        else:
            choixValide = False
    s_comm.send(answer.encode())

# Fermeture de la socket
try:
    s_comm.close()
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')
