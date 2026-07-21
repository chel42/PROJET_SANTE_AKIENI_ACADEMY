# Projet Fil Rouge N°1 — Santé Publique
**Akieni Academy — Programme Data Science 2026**  
**Commanditaire fictif :** Ministère de la Santé de la République du Congo  
**Coordonnateur pédagogique :** Abdias MONTSONGO

---

## Description du Projet

Ce projet fil rouge simule le développement d'un système informatique de gestion sanitaire
pour le Ministère de la Santé de la République du Congo.
Chaque semaine, de nouvelles fonctionnalités sont ajoutées au module fondateur `sante_variables.py`,
qui évolue progressivement vers un produit data professionnel complet.

---

## Structure du Projet

```
Akieni Academy--Exercice/
│
├── Semaine 2/
│   ├── semaine2_exercice1_sante.py     # Fiche patient CHU Brazzaville
│   ├── semaine2_exercice2_sante.py     # KPIs sanitaires OMS — Hôpital Pointe-Noire
│   └── semaine2_challenge.py           # Rapport comparatif 3 hôpitaux du Pool
│
├── Semaine 3/
│   ├── semaine3_exercice1_stocks.py    # Classification stocks médicaments PNA
│   ├── semaine3_exercice2_triage.py    # Triage patient urgences CHU Brazzaville
│   ├── semaine3_challenge.py           # Tableau de bord 5 hôpitaux — Conseil des Ministres
│   └── semaine3_mini_projet.py         # Module sante_variables.py enrichi S3
│
├── Semaine 4/
│   └── semaine4_exercice1_mpox.py      # Surveillance épidémique Mpox — 9 districts
│
├── Semaine 5/
│   └── Projet_S5_Analyse_Ventes_Afrique.ipynb  # Analyse ventes boutique e-commerce Afrique
│
├── Semaine 6/
│   └── Projet_S6_AgriSuds.ipynb        # Digitaliser les récoltes du réseau AgriSuds
│
├── sante_variables.py                  # Module fondateur — constantes, variables, KPIs
├── .gitignore
├── requirements.txt
└── README.md
```

> **CalcX** (calculatrice desktop Flet) — second livrable S5 — est hébergé dans un repo dédié :
> 👉 [github.com/chel42/CalcX](https://github.com/chel42/CalcX)

---

## Semaine 2 — Variables, Types, Opérateurs, f-strings

### Notions couvertes
- Déclaration de variables avec les bons types (`int`, `float`, `str`)
- Opérateurs arithmétiques (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- f-strings pour l'affichage structuré
- `input()` et conversion de types

### Fichiers produits

#### `sante_variables.py` — Module Fondateur
Fichier central du projet. Contient :
- **Section A** : Constantes nationales et normes OMS (taux de change, seuils OMS, 12 départements du Congo)
- **Section B** : Variables des 5 hôpitaux (CHU Brazzaville, Pointe-Noire, Dolisie, Owando, Impfondo)
- **Section C** : Variables des 5 médicaments essentiels (Artemether, Amoxicilline, Paracetamol, SRO, Vaccin)
- **Section D** : Calculs d'initialisation (densité médicale, taux d'occupation moyen, valeur totale du stock)
- **Section E** : Rapport d'inventaire initial

#### `semaine2_exercice1_sante.py` — Fiche Patient CHU Brazzaville
- Contexte : Mme MAVOUNGOU Celestine, 42 ans, urgences CHU Brazzaville
- Calcul du coût total après remise CNSS 30% → **10 500 FCFA**
- Taux d'occupation de l'hôpital → **88.8%**
- Ratio consultations/médecin → **2.6**

#### `semaine2_exercice2_sante.py` — KPIs Sanitaires OMS
- Conversion budget Q4 en EUR et USD
- 3 indicateurs OMS : densité médicale (0.2), taux mortalité (1.4%), taux occupation (79.4%)
- Division entière pour jours de stock médicaments → **68 jours**
- Projection budget N+2 à 8%/an → **102 001 680 FCFA**

#### `semaine2_challenge.py` — Rapport 3 Hôpitaux du Pool
- Comparaison Kinkala, Vindza, Kindamba
- Calcul KPIs : coût moyen/patient, taux occupation, densité médicale, taux mortalité
- Les 3 hôpitaux identifiés en situation critique
- Bonus : analyse budget recrutement 5 médecins/hôpital

---

## Semaine 3 — Conditions & Branchements (if / elif / else)

### Notions couvertes
- Structures `if / elif / else` correctement indentées
- Conditions composées avec `and`, `or`, `not`
- Opérateur ternaire
- Valeurs truthy / falsy
- Import de modules Python (`import`, `from ... import`, `sys.path`)
- Bloc `if __name__ == '__main__'`

### Fichiers produits

#### `semaine3_exercice1_stocks.py` — Classification Stocks PNA
Implémentation des 4 règles de classification de la Pharmacie Nationale d'Approvisionnement :
| Statut | Condition | Couleur |
|---|---|---|
| RUPTURE CRITIQUE | stock <= seuil | 🔴 ROUGE |
| ALERTE STOCK | stock <= seuil × 1.5 | 🟠 ORANGE |
| STOCK LIMITÉ | stock <= seuil × 2.0 | 🟡 JAUNE |
| STOCK NORMAL | stock > seuil × 2.0 | 🟢 VERT |

Résultats : **2 ruptures critiques** (SRO, Vaccin), **1 alerte** (Amoxicilline), **1 normal** (Paracetamol)

#### `semaine3_exercice2_triage.py` — Triage Patient Urgences
Protocole Manchester adapté — saisie interactive via `input()` :
| Niveau | Couleur | Déclencheur | Délai |
|---|---|---|---|
| 1 — IMMÉDIAT | 🔴 ROUGE | temp > 39.5 OU SpO2 < 90 OU tension > 180 | 0 min |
| 2 — URGENT | 🟠 ORANGE | temp > 38.5 OU SpO2 < 94 OU tension > 140 | < 10 min |
| 3 — URGENT DIFFÉRÉ | 🟡 JAUNE | temp > 37.5 OU douleur > 6 | < 30 min |
| 4 — MOINS URGENT | 🟢 VERT | tous paramètres normaux | < 120 min |

#### `semaine3_challenge.py` — Tableau de Bord 5 Hôpitaux
Rapport pour le Conseil des Ministres — Dr. ELENGA Pascal, DSS :
- **4 hôpitaux sur 5** en situation CRITIQUE
- **8 ruptures de stock** identifiées à l'échelle nationale
- Coût commandes urgentes estimé : **3 600 000 FCFA**

#### `semaine3_mini_projet.py` — Module sante_variables.py enrichi S3
Nouvelles sections ajoutées au module fondateur :
- **Section F** : Classification automatique statut stocks (5 médicaments)
- **Section G** : Classification niveau d'occupation (5 hôpitaux)
- **Section H** : Classification couverture vaccinale (4 départements)
- **Section I** : Rapport d'état global avec compteurs d'alertes et résumé exécutif

---

## Semaine 4 — Boucles for, range(), Accumulateurs

### Notions couvertes
- Boucle `for` avec `range()`
- Accumulateurs (initialisation à 0 avant la boucle, addition à chaque tour)
- Compteurs de catégories (zones VERT / JAUNE / ORANGE / ROUGE)
- Combinaison boucle + `if/elif/else` (S3) + `input()` (S2)
- Calcul de taux de létalité avec protection division par zéro

### Fichiers produits

#### `semaine4_exercice1_mpox.py` — Surveillance Épidémique Mpox
- **Contexte réel** : données officielles OMS / Ministère de la Santé Congo, 06/02/2025
- Analyse des 9 districts sanitaires répartis dans 5 départements
- Saisie interactive via `input()` pour chaque district (nom, suspects, confirmés, décès)
- Calcul automatique des cas actifs et du taux de létalité par district
- Classification par niveau d'alerte selon les confirmés :

| Confirmés | Niveau | Couleur |
|---|---|---|
| = 1 | VERT | 🟢 Surveillance standard |
| 2 à 4 | JAUNE | 🟡 Renforcer la surveillance |
| 5 à 9 | ORANGE | 🟠 Envoyer une équipe d'intervention |
| ≥ 10 | ROUGE | 🔴 URGENCE — intervention immédiate |

Résultats nationaux :
- **Total confirmés** : 26 cas | **Total suspects** : 27
- **Zones ROUGE** : 1 (Mossaka-Loukolela — 12 cas)
- **Zones JAUNE** : 4 (Owando, Oyo-Alima, Impfondo, Gamboma)
- **Zones VERT** : 4 (Enyellé-Bétou, Lumumba, Mvou-mvou, Poto-Poto)
- **Zones ORANGE** : 0 | **Total décès** : 0 | **Létalité** : 0.0%

---

## Semaine 5 — Fonctions Python (def, return, try/except, docstrings)

### Notions couvertes
- Définition de fonctions avec `def` et `return`
- Docstrings (documentation des fonctions)
- Portée des variables (scope local / global)
- Gestion des erreurs avec `try / except`
- Architecture multi-fichiers et séparation des responsabilités
- Jupyter Notebook comme environnement d'analyse

### Fichiers produits

#### `Projet_S5_Analyse_Ventes_Afrique.ipynb` — Analyse Ventes Boutique E-commerce
- Données simulées d'une boutique en ligne sur 6 mois dans 5 villes d'Afrique (Dakar, Abidjan, Douala, Brazzaville, Lomé)
- **Niveau Débutant** : 4 fonctions — chiffre d'affaires total, quantité par produit, produit le plus vendu, ventes par ville
- **Niveau Intermédiaire** : 4 fonctions avec `try/except` — CA par mois, panier moyen par ville, filtrage par seuil, détection des anomalies
- Visualisation automatique : graphique CA par mois + quantités vendues par produit

#### `CalcX` — Calculatrice Moderne & Adaptative (repo dédié)
- Application desktop développée avec le framework **Flet** en Python
- Interface responsive adaptée à toutes les tailles d'écran (PC, Tablette, Mobile)
- Architecture modulaire : séparation logique de calcul / gestion d'état / interface graphique
- 👉 **Repo dédié** : [github.com/chel42/CalcX](https://github.com/chel42/CalcX)

---

## Semaine 6 — Structures de données (listes, tuples, dictionnaires, sets)

### Notions couvertes
- **Listes** : stockage et parcours de collections de données avec index
- **Tuples** : retourner plusieurs résultats à la fois depuis une fonction (fourchette de prix, etc.)
- **Dictionnaires** : construire des fiches de synthèse et répartitions en pourcentage
- **Sets** : obtenir instantanément les valeurs uniques sans doublon (cultures, antennes)
- Combinaison de toutes les notions S2 → S6 dans un projet complet

### Fichiers produits

#### `Projet_S6_AgriSuds.ipynb` — Digitaliser les Récoltes du Réseau Coopératif AgriSuds
AgriSuds est un réseau coopératif qui accompagne des petits producteurs agricoles dans plusieurs pays d'Afrique centrale et de l'Ouest, avec 5 antennes locales : Owando (Congo-Brazzaville), Divo (Côte d'Ivoire), Bafoussam (Cameroun), Kaolack (Sénégal), Kpalime (Togo).

Les données de 50 récoltes simulées sont fournies sous forme de 7 listes parallèles (`AGRICULTEURS`, `ANTENNES`, `CULTURES`, `QUANTITES_KG`, `PRIX_KG_FCFA`, `JOURS_ECOULE`). Environ 8% des quantités sont manquantes (`None`) pour simuler les oublis de saisie terrain — toutes les fonctions gèrent ce cas sans planter.

**10 fonctions construites en 3 niveaux :**

| Niveau | Fonction | Rôle |
|---|---|---|
| Débutant | `chiffre_affaires_total` | CA total de toutes les récoltes |
| Débutant | `quantite_totale_culture` | Quantité récoltée pour une culture donnée |
| Débutant | `nombre_recoltes_antenne` | Nombre de récoltes par antenne |
| Intermédiaire | `cultures_et_antennes_uniques` | Sets des cultures et antennes sans doublon |
| Intermédiaire | `fourchette_prix_culture` | Tuple (prix_min, prix_max) par culture |
| Intermédiaire | `fiche_producteur` | Dictionnaire complet d'un producteur |
| Avancé | `top_n_producteurs` | Classement des n meilleurs producteurs |
| Avancé | `recoltes_recentes` | CA des récoltes des X derniers jours |
| Avancé | `repartition_par_culture_pourcentage` | Part (%) de chaque culture dans la production |
| Bonus | `producteur_plus_actif_par_antenne` | Meilleur producteur par antenne |

Visualisation automatique générée : quantité par culture, quantité par antenne, camembert de répartition, top 5 producteurs.

---

## Technologies utilisées
- **Langage** : Python 3.12
- **Environnements** : VS Code, Jupyter Notebook
- **Frameworks** : Flet (CalcX)
- **Versioning** : Git / GitHub

## Comment exécuter

```bash
# Cloner le repo
git clone https://github.com/chel42/PROJET_SANTE_AKIENI_ACADEMY.git

# Lancer un script Python
cd "Akieni Academy--Exercice/Semaine 2"
python sante_variables.py

# Ouvrir un notebook
cd "Semaine 6"
jupyter notebook Projet_S6_AgriSuds.ipynb
```

---

## Progression cumulative

| Semaine | Notions | Statut |
|---|---|---|
| S2 | Variables, types, opérateurs, f-strings, input() | ✅ Terminé |
| S3 | if / elif / else, and / or / not, import | ✅ Terminé |
| S4 | Boucles for, range(), accumulateurs | ✅ Terminé |
| S5 | Fonctions, def, return, try/except, docstrings | ✅ Terminé |
| S6 | Listes, tuples, dictionnaires, sets | ✅ Terminé |


---

*Projet pédagogique — Akieni Academy, Brazzaville, République du Congo — 2026*
