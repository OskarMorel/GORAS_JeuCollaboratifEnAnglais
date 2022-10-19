import socket

# ce qu'il faut pour se connecter au serveur
s=socket.socket()
host=''
port=12000
# connexion en local pour les tests
s.connect(("127.0.0.1",port))
print("You are connected to the server")

# s.send(data)

# messageARecevoir = s.recv(1024).decode()
# print(messageARecevoir)