import csv

# ============================================================
# ÉTAPE 1 : Lire le fichier ventes.csv
# ============================================================

print("=" * 50)
print("       ANALYSE DES VENTES E-COMMERCE")
print("=" * 50)

ca_total = 0  # Pour accumuler le CA Net de toutes les lignes

with open("ventes.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)  # Lit les colonnes par leur nom

    for ligne in reader:

        # Récupérer les valeurs de chaque colonne
        id_produit = ligne["ID"]
        prix       = float(ligne["Prix"])
        quantite   = int(ligne["Quantite"])
        remise     = float(ligne["Remise"])

        # --------------------------------------------------------
        # ÉTAPE 2 : Calculer le Chiffre d'Affaires Brut
        # CA Brut = Prix × Quantité
        # --------------------------------------------------------
        ca_brut = prix * quantite

        # --------------------------------------------------------
        # ÉTAPE 3 : Appliquer la remise pour obtenir le CA Net
        # CA Net = CA Brut × (1 - Remise)
        # Exemple : remise de 0.10 = 10% de réduction
        # --------------------------------------------------------
        ca_net = ca_brut * (1 - remise)

        # --------------------------------------------------------
        # ÉTAPE 4 : Calculer la TVA (20%) sur le CA Net
        # TVA = CA Net × 0.20
        # --------------------------------------------------------
        tva = ca_net * 0.20

        # Ajouter le CA Net au total général
        ca_total += ca_net

        # Afficher les détails de chaque ligne
        print(f"Produit {id_produit} | CA Brut : {ca_brut:.2f} € | "
              f"Remise : {remise*100:.0f}% | CA Net : {ca_net:.2f} € | "
              f"TVA : {tva:.2f} €")

# ============================================================
# ÉTAPE 5 : Afficher le CA Total de l'entreprise
# ============================================================
print("=" * 50)
print(f"  CA TOTAL DE L'ENTREPRISE : {ca_total:.2f} €")
print("=" * 50)