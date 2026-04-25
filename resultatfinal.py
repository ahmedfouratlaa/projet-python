import pandas as pd
import csv
 
rows = []
 
with open("ventes.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
 
        # Récupérer les valeurs
        prix     = float(ligne["Prix"])
        quantite = int(ligne["Quantite"])
        remise   = float(ligne["Remise"])
        ca_brut = round(prix * quantite, 2)
        ca_net = round(ca_brut * (1 - remise), 2)
        tva = round(ca_net * 0.20, 2)
        ligne["CA_Brut"] = ca_brut
        ligne["CA_Net"]  = ca_net
        ligne["TVA"]     = tva
 
        rows.append(ligne)
with open("resultat_finale.csv", mode="w", newline="") as fichier:

    fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]
 
    writer = csv.DictWriter(fichier, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print("Fichier resultat_finale.csv créé avec succès !")
print(f"Il contient {len(rows)} lignes.")
print("Colonnes : ID, Prix, Quantite, Remise, CA_Brut, CA_Net, TVA")
pd.read_csv("resultat_finale.csv")