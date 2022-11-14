import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\sae\jeuCollabTest\Joueur2\QA.json') as mon_fichier:
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

while ok :
    reponseServeur = s.recv(1024).decode()
    # Arret de la boucle si arriver a la fin de l'arbre sinon continue à communiquer
    if reponseServeur == "0":
        # Afficher la reponse envoyer par le serveur
        if data[cleAEnvoyerAuServeur]["reponse1"]["cleNext"] == reponseServeur:
            print(data[cleAEnvoyerAuServeur]["reponse1"]["reponse"])
        else:
            print(data[cleAEnvoyerAuServeur]["reponse2"]["reponse"])
        print("")
        print("Vous etes arriver à la fin du jeux")
        print("")
        ok = False
    elif(cleAEnvoyerAuServeur != "0"):
        print("")
        print("question :")
        # Afficher la reponse envoyer par le serveur
        if data[cleAEnvoyerAuServeur]["reponse1"]["cleNext"] == reponseServeur:
            print(data[cleAEnvoyerAuServeur]["reponse1"]["reponse"])
        else:
            print(data[cleAEnvoyerAuServeur]["reponse2"]["reponse"])

        print("")
        print("1)", data[reponseServeur]["question1"]["question"])
        try:
            print("2)", data[reponseServeur]["question2"]["question"])
        except:
            print("")

        
        
        choix = input("Choose between 1 and 2 : ")

        
        if choix == "1":
            cleAEnvoyerAuServeur = data[reponseServeur]["question1"]["cleNext"]
        elif choix == "2":
            cleAEnvoyerAuServeur = data[reponseServeur]["question2"]["cleNext"]
        else:
            while(choix != "1" and choix !="2"):
                choix = input("Choose between 1 and 2 : ")       
                if choix == "1":
                    cleAEnvoyerAuServeur = data[reponseServeur]["question1"]["cleNext"]
                elif choix == "2":
                    cleAEnvoyerAuServeur = data[reponseServeur]["question2"]["cleNext"]


        s.send(cleAEnvoyerAuServeur.encode())
    else:
        print("")
        print("Vous etes arriver à la fin du jeux")
        print("")
        ok = False
    


# Fermeture de la socket
try:
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')