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

cleDepart = "1"

# Envoi de la première question au serveur (DSI)
cleAEnvoyerAuServeur = cleDepart
print(cleAEnvoyerAuServeur)
s.send(cleAEnvoyerAuServeur.encode())

ok = True
choixAFaire = True

# Explication du contexte du jeu
print("\nYou are a cybersecurity expert, a new client calls you because his company has been hacked.\nThrough different questions you will have to understand how he got hacked and how you can help him.\nGood luck to you\n")

while ok :
    question2 = True
    reponseServeur = s.recv(1024).decode()
    # Arret de la boucle si arriver a la fin de l'arbre sinon continue à communiquer
    if reponseServeur == "0":
        # Afficher la reponse envoyer par le serveur
        if data[cleAEnvoyerAuServeur]["reponse1"]["cleNext"] == reponseServeur:
            print(data[cleAEnvoyerAuServeur]["reponse1"]["reponse"])
        else:
            print(data[cleAEnvoyerAuServeur]["reponse2"]["reponse"])
        print("\nThis is the end of the game\n")
        ok = False
    elif(cleAEnvoyerAuServeur != "0"):
        print("\nquestion :")
        # Afficher la reponse envoyer par le serveur
        if data[cleAEnvoyerAuServeur]["reponse1"]["cleNext"] == reponseServeur:
            print(data[cleAEnvoyerAuServeur]["reponse1"]["reponse"])
        else:
            print(data[cleAEnvoyerAuServeur]["reponse2"]["reponse"])

        print("\n1)", data[reponseServeur]["question1"]["question"])
        try:
            print("2)", data[reponseServeur]["question2"]["question"])
        except:
            print("")
            question2 = False

        choix = input("Choose between 1 and 2 : ")
 
        if choix == "1":
            cleAEnvoyerAuServeur = data[reponseServeur]["question1"]["cleNext"]
        elif choix == "2" and question2 == True:
            cleAEnvoyerAuServeur = data[reponseServeur]["question2"]["cleNext"]
        else:
            while(choix != "1" and choix !="2" or question2 == False):
                choix = input("Choose between 1 and 2 : ")       
                if choix == "1":
                    cleAEnvoyerAuServeur = data[reponseServeur]["question1"]["cleNext"]
                    question2 = True
                elif choix == "2" and question2 == True:
                    cleAEnvoyerAuServeur = data[reponseServeur]["question2"]["cleNext"]

        s.send(cleAEnvoyerAuServeur.encode())
    else:
        print("\nThis is the end of the game\n")
        ok = False

# Fermeture de la socket    
try:
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')