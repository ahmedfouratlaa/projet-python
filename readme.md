#  Analyse Automatisée des Ventes E-Commerce

> Script Python qui génère et analyse automatiquement des données de ventes
> pour remplacer un fichier Excel devenu trop volumineux.

---

## 1.  Titre & Description

**Qu'est-ce que c'est ?**

Ce projet est réalisé dans le cadre d'un TP Python. Une entreprise de e-commerce
utilise un fichier Excel pour suivre ses ventes, mais le volume de données devient
trop important pour un tableur classique.

Ce script Python permet de :
- Générer automatiquement un fichier `ventes.csv` avec des données aléatoires
- Stocker les informations de chaque vente : ID, Prix, Quantité, Remise
- Préparer les données pour une future analyse automatisée

---

## 2.  Prérequis

**Logiciels nécessaires :**

- [Python 3.x](https://www.python.org/downloads/) — langage de programmation utilisé
- [VS Code](https://code.visualstudio.com/) — éditeur de code recommandé

**Extensions VS Code recommandées :**

- Python *(Microsoft)*
- Rainbow CSV *(affiche le CSV en couleurs)*

**Bibliothèques Python utilisées :**

| Bibliothèque | Utilité | Incluse par défaut |
|---|---|---|
| `csv` | Lire et écrire des fichiers CSV | Oui |
| `random` | Générer des données aléatoires | Oui |

>  Aucune installation de bibliothèque supplémentaire n'est nécessaire pour ce projet.

---

## 3.  Installation

**Étape 1 — Cloner ou télécharger le projet**

```bash
git clone https://github.com/votre-utilisateur/projet-python.git
```

Ou télécharge le dossier manuellement et ouvre-le dans VS Code.

**Étape 2 — Vérifier que Python est bien installé**

```bash
python --version
```

Tu dois voir quelque chose comme : `Python 3.14.0`

**Étape 3 — Ouvrir le projet dans VS Code**

```
Fichier → Ouvrir le dossier → sélectionner "projet python"
```

---

## 4.  Utilisation

**Lancer le script pour générer le fichier ventes.csv**

Dans le terminal VS Code (`Ctrl + '`) :

```bash
python ventes.py
```

**Résultat attendu dans le terminal :**

```
Fichier ventes.csv généré avec succès !
Il contient 20 lignes + 1 ligne d'en-tête.
Colonnes : ID, Prix, Quantite, Remise
```

**Fichier généré — exemple de contenu :**

```
ID,Prix,Quantite,Remise
101,381.56,5,0.27
102,272.61,8,0.06
103,345.58,7,0.18
...
120,282.11,10,0.16
```

**Structure du projet :**

```
projet python/
│
├── ventes.py       ← script principal à exécuter
├── ventes.csv      ← fichier généré automatiquement
└── README.md       ← documentation du projet
```

---

## 5.  Auteurs:
***Adem Aroud**

***Ahmed Fourat Laajimi**

***Eya Ben Rebah**

***Mohamed Khalil Chihaoui**


Projet réalisé dans le cadre du cours **Imène Amira — 2025-2026**.