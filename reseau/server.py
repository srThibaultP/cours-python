import socket, threading
from urllib import response

class setup(threading.Thread, socket.socket):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Démarrage du serveur")
        while True :
            socket.listen(5)
            client, address = socket.accept()
            print("Nv connection : ", address)
            
            response = client.recv(255)
            if response != "":
                print(response.decode("utf-8"))
    
    def stop(self):
        print("Arrêt du serveur")
        socket.close()
        threading.Thread.stop(self)

print("Initialisation du serveur")
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.43.67', 15555))
srv = setup()
srv.run()