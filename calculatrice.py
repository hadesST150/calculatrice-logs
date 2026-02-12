import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        return None
    return a / b

logging.info("Démarrage du programme")

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
print("Résultat de l'addition :", resultat_addition)
logging.info(f"Addition de {x} et {y}" )

resultat_division = division(x, y)
if resultat_division is not None:
    print("Résultat de la division :", resultat_division)
    logging.info(f"Division de {x} par {y}")
else:
    print("Division impossible")
    logging.error("Erreur : valeur incorrecte")
    
logging.info("Fin du programme")