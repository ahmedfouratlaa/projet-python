import csv
 
# ============================================================
# ÉTAPE 4 : Calculer la TVA (20%) sur le CA Net
# TVA = CA Net × 0.20
# ============================================================
 
rows = []
 
with open("etape3_ca_net.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
        ca_net = float(ligne["CA_Net"])
 
        tva = round(ca_net * 0.20, 2)
 
        ligne["TVA"] = tva
        rows.append(ligne)
 
with open("etape4_tva.csv", mode="w", newline="") as fichier:
    fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net", "TVA"]
    writer = csv.DictWriter(fichier, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
 
print("etape4_tva.csv créé avec succès !")