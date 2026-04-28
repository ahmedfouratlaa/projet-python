# Automatisation des Ventes

Analyse automatique des ventes à partir d'un fichier CSV.

---

## 1. Titre & Description
Ce projet est un notebook Jupyter développé en **Python**.  
Il génère un fichier `ventes.csv`, effectue les calculs financiers  
et visualise les résultats avec Matplotlib.

Fonctionnalités :
- Génération automatique de `ventes.csv`
- Calcul du CA Brut, CA Net et TVA
- Affichage du CA Total
- Identification du meilleur produit
- Visualisation avec graphiques Matplotlib

---

## 2. Prérequis
- Python 3.x
- Jupyter Notebook

---

## 3. Installation
```bash
# Cloner le projet
git clone https://github.com/ahmedfouratlaa/projet-python.git
cd projet-python

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
jupyter notebook
```

---

## 4. Utilisation
Ouvrir le fichier `Analyse_Ventes.ipynb`  
Exécuter les cellules **dans l'ordre** de haut en bas.

Format du fichier `ventes.csv` généré :

ID,Prix,Quantite,Remise

1,150.50,3,10

2,200.00,2,5


---

## 5. Auteurs
- Eya Ben Rebah
- Ahmed Fourat Laajimi
- Adem Aroud
- Khalil Mohamed Chihaoui

**Encadrante : Imene Amira**
