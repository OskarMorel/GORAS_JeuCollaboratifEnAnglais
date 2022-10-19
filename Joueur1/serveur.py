import socket
import os
import sys
import json

# Tout ce qu'il faut pour se mettre en place le serveur
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=12000
s.bind(("",port))
hostname = socket.gethostname()
s.listen(10)

serveurOn = True
# communication avec le client
c, addr = s.accept()
print("Client connected", addr)
content = c.recv(1024).decode()



# s'arrête quand le client et le serveur on échangé
# //TODO faire une boucle tant que pas appuyé sur une certainte touche qui mets fin au jeu et donc au serveur
s.close()
