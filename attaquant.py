import socket
import time

HOST = "127.0.0.1"
PORT = 6000

def attaquer(nb_tentatives):
    for i in range(nb_tentatives):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((HOST, PORT))
        except:
            pass
        client.close()
        time.sleep(1)

if __name__ == "__main__":
    attaquer(10)