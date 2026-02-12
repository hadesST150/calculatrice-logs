import os
import logging
import datetime

# Configuration du logging
logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def verifier_connectivite(hote):
    logging.info(f"Test de connectivité vers {hote}")

    # -c pour Linux / -n pour Windows
    param = "-n" if os.name == "nt" else "-c"
    commande = f"ping {param} 1 {hote}"

    reponse = os.system(commande)

    if reponse == 0:
        logging.info(f"{hote} est accessible")
        return True
    else:
        logging.warning(f"{hote} ne répond pas")
        return False

def verifier_charge_cpu():
    logging.info("Simulation vérification charge CPU")
    charge = 30  # valeur fictive
    if charge > 80:
        logging.warning("Charge CPU élevée")
    return charge


if __name__ == "__main__":
    verifier_connectivite("127.0.0.1")