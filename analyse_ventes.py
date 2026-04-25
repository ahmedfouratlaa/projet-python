import csv
print("=" * 50)
print("       ANALYSE DES VENTES E-COMMERCE")
print("=" * 50)

ca_total = 0  # Pour accumuler le CA Net de toutes les lignes

with open("ventes.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)  # Lit les colonnes par leur nom

    for ligne in reader:
        id_produit = ligne["ID"]
        prix       = float(ligne["Prix"])
        quantite   = int(ligne["Quantite"])
        remise     = float(ligne["Remise"])
        ca_brut = prix * quantite
        ca_net = ca_brut * (1 - remise)
        tva = ca_net * 0.20
        ca_total += ca_net
        print(f"Produit {id_produit} | CA Brut : {ca_brut:.2f} € | "
              f"Remise : {remise*100:.0f}% | CA Net : {ca_net:.2f} € | "
              f"TVA : {tva:.2f} €")

print("=" * 50)
print(f"  CA TOTAL DE L'ENTREPRISE : {ca_total:.2f} €")
print("=" * 50)