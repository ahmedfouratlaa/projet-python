import pandas as pd
import csv
import random
 
# ============================================================
#  ÉTAPE 1 : Ouvrir (ou créer) le fichier ventes.csv
# ============================================================
# "w"        = mode écriture (write)
# newline="" = évite les lignes vides entre chaque ligne sur Windows
# ============================================================
 
with open("ventes.csv", mode="w", newline="") as fichier:
 
    # On crée un "writer" : c'est lui qui va écrire dans le fichier
    writer = csv.writer(fichier)
 
    # --------------------------------------------------------
    # ÉTAPE 2 : Écrire la ligne d'en-tête (les noms des colonnes)
    # --------------------------------------------------------
    writer.writerow(["ID", "Prix", "Quantite", "Remise"])
 
    # --------------------------------------------------------
    # ÉTAPE 3 : Générer 100 lignes de données aléatoires
    # --------------------------------------------------------
    # range(1, 101) génère les nombres de 1 à 100
    # À chaque tour de boucle, "i" représente l'ID du produit
 
    for i in range(1, 50):
 
        # Prix aléatoire entre 10 € et 500 €, arrondi à 2 décimales
        prix = round(random.uniform(10, 500), 2)
 
        # Quantité aléatoire entre 1 et 10 (nombre entier)
        quantite = random.randint(1, 10)
 
        # Remise aléatoire entre 0% et 30%, arrondie à 2 décimales
        # Exemple : 0.15 signifie une remise de 15%
        remise = round(random.uniform(0, 0.3), 2)
 
        # On écrit la ligne dans le fichier CSV
        writer.writerow([i, prix, quantite, remise])
 
# ============================================================
#  ÉTAPE 4 : Confirmer que tout s'est bien passé
# ============================================================
print("Fichier ventes.csv généré avec succès !")
print("Il contient 100 lignes + 1 ligne d'en-tête.")
print("Colonnes : ID, Prix, Quantite, Remise")
pd.read_csv("ventes.csv")