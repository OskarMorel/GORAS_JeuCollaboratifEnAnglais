import socket
import json

# Ouverture du fichier JSON qui contient les questions / réponses
with open('Z:\sae\jeuCollabTest\Joueur1\QA.json') as QA:
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
print("Connection etablie\n")

ok = True
premier = False
choixAFaire = True

while ok :
    receptionClient = s_comm.recv(1024).decode()
    print("reception du client : ", receptionClient)

    if receptionClient != "0":

        if premier:
            if data[cleAEnvoyer]["question1"]["cleNext"] == receptionClient:
                print(data[cleAEnvoyer]["question1"]["question"])
            else:
                print(data[cleAEnvoyer]["question2"]["question"])
        else:
            print(data["1"]["question"])

        # Choix de la réponse à envoyer au client (l'expert en cybersécurité)
        print("1) " + data[receptionClient]["reponse1"]["reponse"])
        try:
            print("2) " + data[receptionClient]["reponse2"]["reponse"])
        except:
            print("")
        
        
        choix = input("Choose between 1 and 2 : ")
        if choix == "1":
            cleAEnvoyer = data[receptionClient]["reponse1"]["cleNext"]
        elif choix == "2":
            cleAEnvoyer = data[receptionClient]["reponse2"]["cleNext"]
        else:
            while(choix != "1" and choix !="2"):
                    choix = input("Choose between 1 and 2 : ")       
                    if choix == "1":
                        cleAEnvoyer = data[receptionClient]["reponse1"]["cleNext"]
                    elif choix == "2":
                        cleAEnvoyer = data[receptionClient]["reponse2"]["cleNext"]


        print("")
        print("clé a envoyer au serveur", cleAEnvoyer)
        print("")
        premier = True
        # Arret de la boucle si arriver a la fin de l'arbre
        if cleAEnvoyer == "0":
            print("")
            print("Vous etes arriver à la fin du jeux")
            print("")
            ok = False
        s_comm.send(cleAEnvoyer.encode())
    else:
        print("")
        print("Vous etes arriver à la fin du jeux")
        print("")
        ok = False




# Fermeture de la socket
try:
    s_comm.close()
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')
