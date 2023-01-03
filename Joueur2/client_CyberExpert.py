# +----------------------------------------------------------------------------------------------------------------------+
# | Author : Morel Oskar                                                                                                 |
# |          Gouzy Antoine                                                                                               |
# |          Jauzion Rémi                                                                                                |
# |          Gauthier Jalbaud                                                                                             |
# |          Launay Simon                                                                                                 |
# +----------------------------------------------------------------------------------------------------------------------+
# | CyberExpert / client :                                                                                               |
# | - Envoie des question au DSI (Joueur1 / serveur)                                                                     |
# | - Utilisation des sockets en TCP.                                                                                    |
# | - Coupage du code en plusieurs fonctions.                                                                            |
# | - Gestion des erreurs avec des try / except                                                                          |
# | - Le client (ce programme) doit entrer l'IP du serveur pour s'y connecter (le serveur affiche son IP dans la console |
# +----------------------------------------------------------------------------------------------------------------------+

import socket
import json
import os
import time

print("╔═══╗╔╗                      ╔═══╗")
print("║╔═╗║║║                      ║╔═╗║")
print("║╚═╝║║║ ╔══╗ ╔╗ ╔╗╔══╗╔═╗    ╚╝╔╝║")
print("║╔══╝║║ ╚ ╗║ ║║ ║║║╔╗║║╔╝    ╔═╝╔╝")
print("║║   ║╚╗║╚╝╚╗║╚═╝║║║═╣║║     ║║╚═╗")
print("╚╝   ╚═╝╚═══╝╚═╗╔╝╚══╝╚╝     ╚═══╝")
print("             ╔═╝║")
print("             ╚══╝")

# Utilisés dans les échanges avec le client
QUESTION_1 = "question1"
QUESTION_2 = "question2"
QUESTION = "question"
CLE_NEXT = "cleNext"
REPONSE_1 = "reponse1"
REPONSE_2 = "reponse2"
REPONSE = "reponse"

# Récupération du chemin courant pour accéder au fichier des questions / réponses
path = os.getcwd()

# Ouverture du fichier JSON qui contient les questions / réponses
with open(path + '\QA.json') as mon_fichier:
    data = json.load(mon_fichier)

# Création de la socket du client
# return : socketClient = la socket du client
#          coordonneesServeur = les coordonnées du serveur (IP + port)
def creationSocket():
    try:
        socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError:
        print('Socket creation failed')
    else:
        print('Socket creation success')
        coordonneesServeur = (ipServeur, 65432)
    return(socketClient, coordonneesServeur)

# Acceptation de la connexion avec le serveur (DSI)
# ----- Paramètre : socketClient = la socket crée par la fonction creationSocket() -----
#                   coordonneesServeur : les coordonnées (IP + port) du serveur afin de pouvoir se connecter à celui ci
def connecter(socketClient, coordonneesServeur):
    print ("Waiting for connection\n")
    socketClient.connect(coordonneesServeur)
    print("connection established")

cleDepart = "1"

# S'occupe de la connectionActuelle avec le serveur (Récupération de la question + réponse à celle ci)
# ----- Paramètres : socketServeur = la socket créée par la foncion creationSocket() -----
def programmePrincipal(socketClient):
    # Envoi de la première question au serveur (DSI)
    cleAEnvoyerAuServeur = cleDepart
    socketClient.send(cleAEnvoyerAuServeur.encode())

    ok = True
    choixAFaire = True

    # Explication du contexte du jeu
    print("\nYou are a cybersecurity expert, a new client calls you because his company has been hacked.\nThrough different questions you will have to understand how he got hacked and how you can help him.\nGood luck to you\n")
    while ok :
        question2 = True
        reponseServeur = socketClient.recv(1024).decode()
        # Arret de la boucle si arriver a la fin de l'arbre sinon continue à communiquer
        if reponseServeur == "0":
            # Afficher la reponse envoyer par le serveur
            if data[cleAEnvoyerAuServeur][REPONSE_1][CLE_NEXT] == reponseServeur:
                print(data[cleAEnvoyerAuServeur][REPONSE_1][REPONSE])
            else:
                print(data[cleAEnvoyerAuServeur][REPONSE_2][REPONSE])
            print("\nThis is the end of the game\n")
            ok = False
        elif(cleAEnvoyerAuServeur != "0"):
            print("\nquestion :")
            # Afficher la reponse envoyer par le serveur
            if data[cleAEnvoyerAuServeur][REPONSE_1][CLE_NEXT] == reponseServeur:
                print(data[cleAEnvoyerAuServeur][REPONSE_1][REPONSE])
            else:
                print(data[cleAEnvoyerAuServeur][REPONSE_2][REPONSE])

            print("\n1)", data[reponseServeur][QUESTION_1][QUESTION])
            try:
                print("2)", data[reponseServeur][QUESTION_2][QUESTION] + "\n")
            except:
                print("")
                question2 = False

            choix = input("Choose between 1 and 2 : ")
    
            # Choix de la question à envoyer
            if choix == "1":
                cleAEnvoyerAuServeur = data[reponseServeur][QUESTION_1][CLE_NEXT]
            elif choix == "2" and question2 == True:
                cleAEnvoyerAuServeur = data[reponseServeur][QUESTION_2][CLE_NEXT]
            else:
                # Boucle qui gère l'erreur (si il appuye sur autre que que 1 ou 2 redemande)
                while(choix != "1" and choix !="2" or question2 == False):
                    choix = input("Choose between 1 and 2 : ")       
                    if choix == "1":
                        cleAEnvoyerAuServeur = data[reponseServeur][QUESTION_1][CLE_NEXT]
                        question2 = True
                    elif choix == "2" and question2 == True:
                        cleAEnvoyerAuServeur = data[reponseServeur][QUESTION_2][CLE_NEXT]

            socketClient.send(cleAEnvoyerAuServeur.encode())
        else:
            print("\nThis is the end of the game\n")
            ok = False

# Ferme la connection avec le client et ferme la socket
# ----- Parametres : socketServeur = la socket créée par la fonction creationSocket()
def fermetureSocket(socketClient):  
    try:
        socketClient.close()
    except OSError:
        print('Socket open!')
    else:
        print('Socket closed')

while True:
    try:
        ipServeur = input("Please, write the server's IP : ")
        socketClient, coordonneesServeur = creationSocket()
        connecter(socketClient, coordonneesServeur) 
        break
    except socket.error:
        print("Oops! That was no a valid IP!...Try again!")

programmePrincipal(socketClient)
print("\nThe application will close in 10 seconds")
time.sleep(10.0)
fermetureSocket(socketClient)