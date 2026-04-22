import csv
 
# ============================================================
# ÉTAPE 2 : Calculer le Chiffre d'Affaires Brut
# CA Brut = Prix × Quantité
# ============================================================
 
rows = []
 
with open("ventes.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
        prix     = float(ligne["Prix"])
        quantite = int(ligne["Quantite"])
 
        ca_brut = round(prix * quantite, 2)
 
        ligne["CA_Brut"] = ca_brut
        rows.append(ligne)
 
with open("etape2_ca_brut.csv", mode="w", newline="") as fichier:
    fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut"]
    writer = csv.DictWriter(fichier, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
 
print("etape2_ca_brut.csv créé avec succès !")