import socket
import json

with open('Z:\GORAS_JeuCollaboratifEnAnglais\Joueur1\QA.json') as QA:
    data = json.load(QA)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Description socket : ', s)
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
print("The Cybersecurity expert is ready talk with you !!\n")

question = s_comm.recv(1024)
print("Question : " + question.decode())
print("\n***************************************")

ok = False
while ok == False:
    print("1 : " + data["1"]["reponse1"]["reponse"])
    print("2 : " + data["1"]["reponse2"]["reponse"])
    answer = input("Choose between 1 and 2 : ")
    if answer == "1":
        ok = True
    elif answer == "2":
        ok = True
    else:
        ok = False

s_comm.send(answer.encode())

try:
    s_comm.close()
    s.close()
except OSError:
    print('Socket encore ouverte !')
else:
    print('Socket correctement fermée')
