# ============================================================
# AKIENI ACADEMY - Semaine 6 - Projet Autonome
# Gestionnaire de Budget Personnel
# Notions : S2 (variables, f-strings) + S3 (if/elif/else)
#          + S4 (boucles for) + S5 (fonctions def/return)
#          + S6 (listes, dictionnaires, sets, tuples)
# ============================================================

# ============================================================
# SECTION 1 : DONNEES — Listes paralleles des depenses
# ============================================================

CATEGORIES_DISPONIBLES = ['Alimentation', 'Transport', 'Loyer', 'Sante', 'Loisirs', 'Habillement', 'Autre']

# Listes paralleles — l'element i decrit la meme depense dans chaque liste
descriptions  = []   # str  - description de la depense
categories    = []   # str  - categorie de la depense
montants      = []   # float - montant en FCFA
jours         = []   # int  - jour du mois (1 a 31)

# Budget mensuel fixe par l'utilisateur
BUDGET_MENSUEL = 150_000.0   # FCFA - a adapter selon ta situation

# ============================================================
# SECTION 2 : FONCTIONS DE SAISIE
# ============================================================

def saisir_depenses(nb_depenses):
    """Demande a l'utilisateur de saisir ses depenses une par une."""
    print()
    print('Entrez vos depenses du mois :')
    print('Categories disponibles :', ', '.join(CATEGORIES_DISPONIBLES))
    print()

    for i in range(1, nb_depenses + 1):
        print(f'--- Depense {i} ---')

        # Description
        desc = input('Description : ')
        descriptions.append(desc)

        # Categorie avec validation
        cat = input('Categorie : ').strip().capitalize()
        if cat not in CATEGORIES_DISPONIBLES:
            cat = 'Autre'
            print('  Categorie inconnue - classee dans "Autre"')
        categories.append(cat)

        # Montant avec protection erreur
        try:
            montant = float(input('Montant (FCFA) : '))
            if montant < 0:
                montant = 0.0
                print('  Montant negatif ignore - mis a 0')
        except ValueError:
            montant = 0.0
            print('  Valeur invalide - montant mis a 0')
        montants.append(montant)

        # Jour
        try:
            jour = int(input('Jour du mois (1-31) : '))
            if jour < 1 or jour > 31:
                jour = 1
        except ValueError:
            jour = 1
        jours.append(jour)

        print()

# ============================================================
# SECTION 3 : FONCTIONS D'ANALYSE 
# ============================================================

def total_depenses(montants):
    """Calcule le total de toutes les depenses."""
    total = 0.0
    for montant in montants:
        total = total + montant
    return total


def total_par_categorie(categories, montants):
    """Retourne un dictionnaire {categorie: total_depense}."""
    resultat = {}
    for i in range(len(categories)):
        cat = categories[i]
        if cat not in resultat:
            resultat[cat] = 0.0
        resultat[cat] = resultat[cat] + montants[i]
    return resultat


def categorie_la_plus_depensiere(total_par_cat):
    """
    Retourne un tuple (categorie, montant) de la categorie
    ou on a le plus depense.
    """
    categorie_max = None
    montant_max   = 0.0

    for categorie, montant in total_par_cat.items():
        if montant > montant_max:
            montant_max   = montant
            categorie_max = categorie

    return (categorie_max, montant_max)


def repartition_pourcentage(total_par_cat, total_general):
    """Retourne un dictionnaire {categorie: pourcentage}."""
    repartition = {}
    for categorie, montant in total_par_cat.items():
        if total_general > 0:
            pct = round(montant / total_general * 100, 1)
        else:
            pct = 0.0
        repartition[categorie] = pct
    return repartition


def statut_budget(total_depense, budget):
    """
    Classifie le statut du budget selon les depenses.
    Retourne un tuple (statut, message).
    """
    taux = total_depense / budget * 100

    if taux >= 100:
        statut  = 'DEPASSEMENT'
        message = f'Budget depasse de {round(total_depense - budget):,} FCFA !'.replace(',', ' ')
    elif taux >= 85:
        statut  = 'ATTENTION'
        message = f'Il ne reste que {round(budget - total_depense):,} FCFA'.replace(',', ' ')
    elif taux >= 60:
        statut  = 'NORMAL'
        message = f'Budget maitrise - {round(budget - total_depense):,} FCFA restants'.replace(',', ' ')
    else:
        statut  = 'EXCELLENT'
        message = f'Bonne gestion - {round(budget - total_depense):,} FCFA restants'.replace(',', ' ')

    return (statut, message)


def categories_uniques(categories):
    """Retourne le set des categories effectivement utilisees."""
    uniques = set()
    for cat in categories:
        uniques.add(cat)
    return uniques


def top_3_depenses(descriptions, montants):
    """
    Retourne la liste des 3 depenses les plus elevees
    sous forme de tuples (description, montant).
    """
    paires = []
    for i in range(len(descriptions)):
        paires.append((descriptions[i], montants[i]))

    paires_triees = sorted(paires, key=lambda x: x[1], reverse=True)
    return paires_triees[:3]

# ============================================================
# SECTION 4 : AFFICHAGE DU RAPPORT
# ============================================================

def afficher_rapport():
    """Genere et affiche le rapport complet du budget."""

    #  Calculs 
    total          = total_depenses(montants)
    total_par_cat  = total_par_categorie(categories, montants)
    cat_max        = categorie_la_plus_depensiere(total_par_cat)
    repartition    = repartition_pourcentage(total_par_cat, total)
    statut, msg    = statut_budget(total, BUDGET_MENSUEL)
    top3           = top_3_depenses(descriptions, montants)
    cats_utilisees = categories_uniques(categories)
    reste          = BUDGET_MENSUEL - total

    # Affichage 
    print()
    print('=' * 60)
    print('   RAPPORT DE BUDGET MENSUEL')
    print('=' * 60)

    print(f'\n  Budget fixe     : {BUDGET_MENSUEL:>12,.0f} FCFA'.replace(',', ' '))
    print(f'  Total depense   : {total:>12,.0f} FCFA'.replace(',', ' '))
    print(f'  Reste           : {reste:>12,.0f} FCFA'.replace(',', ' '))
    print(f'  Nb de depenses  : {len(montants)} operations')
    print(f'  Categories      : {len(cats_utilisees)} utilisees sur {len(CATEGORIES_DISPONIBLES)}')

    # Statut budget
    print()
    print('-' * 60)
    if statut == 'DEPASSEMENT':
        print(f'  STATUT : !! {statut} - {msg}')
    elif statut == 'ATTENTION':
        print(f'  STATUT : /!\\ {statut} - {msg}')
    else:
        print(f'  STATUT : OK {statut} - {msg}')

    # Repartition par categorie
    print()
    print('-' * 60)
    print('  REPARTITION PAR CATEGORIE')
    print('-' * 60)

    for cat, montant in sorted(total_par_cat.items(), key=lambda x: x[1], reverse=True):
        pct    = repartition[cat]
        barre  = '#' * int(pct / 2)   # barre proportionnelle
        print(f'  {cat:<15} : {montant:>10,.0f} FCFA  ({pct}%)  {barre}'.replace(',', ' '))

    # Categorie la plus depensiere
    print()
    print(f'  >> Poste le plus eleve : {cat_max[0]} ({cat_max[1]:,.0f} FCFA)'.replace(',', ' '))

    # Top 3 depenses
    print()
    print('-' * 60)
    print('  TOP 3 DEPENSES LES PLUS ELEVEES')
    print('-' * 60)
    for i, (desc, montant) in enumerate(top3, 1):
        print(f'  {i}. {desc:<25} : {montant:>10,.0f} FCFA'.replace(',', ' '))

    print()
    print('=' * 60)

# ============================================================
# SECTION 5 : PROGRAMME PRINCIPAL
# ============================================================

if __name__ == '__main__':
    print('=' * 60)
    print('   GESTIONNAIRE DE BUDGET PERSONNEL')
    print('   Akieni Academy - Semaine 6')
    print('=' * 60)

    # Nombre de depenses a saisir
    try:
        nb = int(input('\nCombien de depenses voulez-vous saisir ? '))
        if nb <= 0:
            nb = 1
    except ValueError:
        nb = 5
        print('Valeur invalide - 5 depenses par defaut')

    # Saisie
    saisir_depenses(nb)

    # Rapport
    afficher_rapport()
