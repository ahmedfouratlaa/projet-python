import pandas as pd
import csv
 
# ============================================================
# ÉTAPE 1 : Lire le fichier ventes.csv
# ============================================================
 
rows = []
 
with open("ventes.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
 
        # Récupérer les valeurs
        prix     = float(ligne["Prix"])
        quantite = int(ligne["Quantite"])
        remise   = float(ligne["Remise"])
 
        # --------------------------------------------------------
        # ÉTAPE 2 : Calculer le CA Brut
        # CA Brut = Prix × Quantité
        # --------------------------------------------------------
        ca_brut = round(prix * quantite, 2)
 
        # --------------------------------------------------------
        # ÉTAPE 3 : Calculer le CA Net (après remise)
        # CA Net = CA Brut × (1 - Remise)
        # --------------------------------------------------------
        ca_net = round(ca_brut * (1 - remise), 2)
 
        # --------------------------------------------------------
        # ÉTAPE 4 : Calculer la TVA (20%)
        # TVA = CA Net × 0.20
        # --------------------------------------------------------
        tva = round(ca_net * 0.20, 2)
 
        # Ajouter les nouvelles colonnes à la ligne
        ligne["CA_Brut"] = ca_brut
        ligne["CA_Net"]  = ca_net
        ligne["TVA"]     = tva
 
        rows.append(ligne)
 
# ============================================================
# ÉTAPE 5 : Écrire le nouveau fichier resultat_finale.csv
# ============================================================
 
with open("resultat_finale.csv", mode="w", newline="") as fichier:
 
    # Définir les colonnes du nouveau fichier
    fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]
 
    writer = csv.DictWriter(fichier, fieldnames=fieldnames)
 
    # Écrire l'en-tête
    writer.writeheader()
 
    # Écrire toutes les lignes
    writer.writerows(rows)
 
# ============================================================
# ÉTAPE 6 : Confirmer la création du fichier
# ============================================================
print("Fichier resultat_finale.csv créé avec succès !")
print(f"Il contient {len(rows)} lignes.")
print("Colonnes : ID, Prix, Quantite, Remise, CA_Brut, CA_Net, TVA")
pd.read_csv("resultat_finale.csv")