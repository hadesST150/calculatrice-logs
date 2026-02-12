import socket
import random
import logging
import time

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "127.0.0.1"
PORT = 5000

def generer_temperature():
    return round(random.uniform(15, 30), 2)

def envoyer_donnee():
    temperature = generer_temperature()
    message = f"temperature:{temperature}"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(message.encode())
    client.close()

    logging.info(f"Donnée envoyée : {message}")

while True:
    envoyer_donnee()
    time.sleep(3)