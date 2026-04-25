import csv
ca_total = 0
 
with open("etape4_tva.csv", mode="r") as fichier:
    reader = csv.DictReader(fichier)
 
    for ligne in reader:
        ca_total += float(ligne["CA_Net"])
 
ca_total = round(ca_total, 2)
 
with open("etape5_ca_total.csv", mode="w", newline="") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["CA_Total"])
    writer.writerow([ca_total])
 
print("=" * 50)
print(f"  CA TOTAL DE L'ENTREPRISE : {ca_total:.2f} €")
print("=" * 50)
print("etape5_ca_total.csv créé avec succès !")
 