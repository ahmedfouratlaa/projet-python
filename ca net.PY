import csv
 
# ============================================================
# ÉTAPE 3 : Appliquer la remise pour obtenir le CA Net
# CA Net = CA Brut × (1 - Remise)
# ============================================================
 
rows = []
 
with open("etape2_ca_brut.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
        ca_brut = float(ligne["CA_Brut"])
        remise  = float(ligne["Remise"])
 
        ca_net = round(ca_brut * (1 - remise), 2)
 
        ligne["CA_Net"] = ca_net
        rows.append(ligne)
 
with open("etape3_ca_net.csv", mode="w", newline="") as fichier:
    fieldnames = ["ID", "Prix", "Quantite", "Remise", "CA_Brut", "CA_Net"]
    writer = csv.DictWriter(fichier, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
 
print("etape3_ca_net.csv créé avec succès !")