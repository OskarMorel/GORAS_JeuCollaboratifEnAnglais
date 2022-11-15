import socket
import json
import os

# Récupération du chemin courant pour accéder au fichier des questions / réponses
path = os.getcwd()

# Ouverture du fichier JSON qui contient les questions / réponses
with open(path + '\QA.json') as QA:

    data = json.load(QA)

# Création de la socket du serveur
def creationSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError:
        print('Socket creation failed')
    else:
        print('Socket creation success')
        coord_S = ('127.0.0.1', 65432)
        # Association des coordonnées à la socket créée 
        try:
            s.bind(coord_S)
            s.listen(1)
        except OSError:
            print('bind() fail')
            s.close()
        else:
            print('bind() success')
    return s

# Acceptation de la connexion avec le client (l'expert en cybersécurité)
def accepter(s):
    (s_comm, coord_C) = s.accept()
    print("connection established\n")
    return(s_comm)



def programmePrincipal(s, s_comm):
    ok = True
    premier = False
    choixAFaire = True
    # Explication du contexte
    print("You are a CIO, your company has been hacked. That's why you called a cybersecurity expert.\nYou will have to answer his questions so that he can help you.\nGood luck.\n")
    while ok :
        question2 = True
        receptionClient = s_comm.recv(1024).decode()

        if receptionClient != "0":
            if premier:
                if data[cleAEnvoyer]["question1"]["cleNext"] == receptionClient:
                    print(data[cleAEnvoyer]["question1"]["question"]+ "\n")
                else:
                    print(data[cleAEnvoyer]["question2"]["question"] + "\n")
            else:
                print(data["1"]["question"])

            # Choix de la réponse à envoyer au client (l'expert en cybersécurité)
            print("1) " + data[receptionClient]["reponse1"]["reponse"])
            try:
                print("2) " + data[receptionClient]["reponse2"]["reponse"] + "\n")
            except:
                print("")
                question2 = False

            choix = input("Choose between 1 and 2 : ")
            if choix == "1":
                cleAEnvoyer = data[receptionClient]["reponse1"]["cleNext"]
            elif choix == "2" and question2 == True:
                cleAEnvoyer = data[receptionClient]["reponse2"]["cleNext"]
            else:
                while(choix != "1" and choix !="2" or question2 == False):
                        choix = input("Choose between 1 and 2 : ")       
                        if choix == "1":
                            cleAEnvoyer = data[receptionClient]["reponse1"]["cleNext"]
                            question2 = True
                        elif choix == "2" and question2 == True:
                            cleAEnvoyer = data[receptionClient]["reponse2"]["cleNext"]

            premier = True
            # Arret de la boucle si arriver a la fin de l'arbre
            if cleAEnvoyer == "0":
                print("\nThis is the end of the game\n")
                ok = False
            s_comm.send(cleAEnvoyer.encode())

        else:
            print("\nThis is the end of the game\n")
            ok = False

# Fermeture de la socket
def fermetureSocket(s, s_comm):
    try:
        s_comm.close()
        s.close()
    except OSError:
        print('Socket encore ouverte !')
    else:
        print('Socket correctement fermée')

s = creationSocket()
s_comm = accepter(s)
programmePrincipal(s, s_comm)
fermetureSocket(s, s_comm)