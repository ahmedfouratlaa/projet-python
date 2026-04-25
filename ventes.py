import pandas as pd
import csv
import random
with open("ventes.csv", mode="w", newline="") as fichier:
 
    writer = csv.writer(fichier)

    writer.writerow(["ID", "Prix", "Quantite", "Remise"])
 
 
    for i in range(1, 50):
        prix = round(random.uniform(10, 500), 2)
        quantite = random.randint(1, 10)
        remise = round(random.uniform(0, 0.3), 2)
        writer.writerow([i, prix, quantite, remise])

print("Fichier ventes.csv généré avec succès !")
print("Il contient 100 lignes + 1 ligne d'en-tête.")
print("Colonnes : ID, Prix, Quantite, Remise")
pd.read_csv("ventes.csv")