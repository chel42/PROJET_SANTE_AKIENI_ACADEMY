# ============================================================
# AKIENI ACADEMY - Semaine 6 - Projet Autonome
# Systeme d'Analyse des Notes d'une Classe 
# Notions : S2 (variables, f-strings) + S3 (if/elif/else)
#          + S4 (boucles for) + S5 (fonctions def/return)
#          + S6 (listes, dictionnaires, tuples)
# ============================================================

# ============================================================
# SECTION 1 : DONNEES - Listes paralleles
# ============================================================

noms_eleves = []   # str   - prenom et nom de l'eleve
notes       = []   # float - note sur 20
matieres    = []   # str   - matiere evaluee

# Seuils de classification des mentions
SEUIL_EXCELLENT  = 16.0
SEUIL_BIEN       = 14.0
SEUIL_ASSEZ_BIEN = 12.0
SEUIL_PASSABLE   = 10.0

NOM_CLASSE = 'Terminale C'
NOM_ECOLE  = 'Lycee de la Paix - Brazzaville'

# ============================================================
# SECTION 2 : FONCTIONS DE SAISIE
# ============================================================

def saisir_notes(nb_eleves, matiere):
    """Saisit les noms et les notes de tous les eleves pour une matiere."""

    print()
    print(f'  Saisie des notes de : {matiere}')
    print('-' * 60)

    for i in range(1, nb_eleves + 1):
        print(f'  Eleve {i} :')
        nom = input('    Nom et prenom : ')

        # Note avec validation
        try:
            note = float(input('    Note /20 : '))
            if note < 0 or note > 20:
                print('    Note hors plage — mise a 0')
                note = 0.0
        except ValueError:
            note = 0.0
            print('    Valeur invalide — note mise a 0')

        noms_eleves.append(nom)
        notes.append(note)
        matieres.append(matiere)
        print()

# ============================================================
# SECTION 3 : FONCTIONS D'ANALYSE
# ============================================================

def attribuer_mention(note):
    """Attribue une mention selon la note."""
    if note >= SEUIL_EXCELLENT:
        return 'Excellent'
    elif note >= SEUIL_BIEN:
        return 'Bien'
    elif note >= SEUIL_ASSEZ_BIEN:
        return 'Assez Bien'
    elif note >= SEUIL_PASSABLE:
        return 'Passable'
    else:
        return 'Insuffisant'


def calculer_moyenne(liste_notes):
    """Calcule la moyenne d'une liste de notes."""
    if len(liste_notes) == 0:
        return 0.0
    total = 0.0
    for note in liste_notes:
        total = total + note
    return round(total / len(liste_notes), 2)


def note_min_max(liste_noms, liste_notes):
    """Retourne deux tuples :(nom_min, note_min) et (nom_max, note_max)"""
    nom_min  = liste_noms[0]
    note_min = liste_notes[0]
    nom_max  = liste_noms[0]
    note_max = liste_notes[0]

    for i in range(len(liste_notes)):
        if liste_notes[i] < note_min:
            note_min = liste_notes[i]
            nom_min  = liste_noms[i]
        if liste_notes[i] > note_max:
            note_max = liste_notes[i]
            nom_max  = liste_noms[i]

    return (nom_min, note_min), (nom_max, note_max)


def compteur_mentions(liste_notes):
    """Retourne un dictionnaire {mention: nombre_eleves}."""
    compteurs = {
        'Excellent'  : 0,
        'Bien'       : 0,
        'Assez Bien' : 0,
        'Passable'   : 0,
        'Insuffisant': 0
    }
    for note in liste_notes:
        mention = attribuer_mention(note)
        compteurs[mention] = compteurs[mention] + 1
    return compteurs


def eleves_en_difficulte(liste_noms, liste_notes):
    """Retourne la liste des tuples (nom, note) des eleves < 10."""
    en_difficulte = []
    for i in range(len(liste_notes)):
        if liste_notes[i] < SEUIL_PASSABLE:
            en_difficulte.append((liste_noms[i], liste_notes[i]))
    return en_difficulte


def classement_top3(liste_noms, liste_notes):
    """Retourne les 3 meilleurs eleves sous forme de tuples (nom, note)."""
    paires = []
    for i in range(len(liste_noms)):
        paires.append((liste_noms[i], liste_notes[i]))
    paires_triees = sorted(paires, key=lambda x: x[1], reverse=True)
    return paires_triees[:3]


def taux_reussite(liste_notes):
    """Calcule le taux de reussite (eleves >= 10) en pourcentage."""
    nb_admis = 0
    for note in liste_notes:
        if note >= SEUIL_PASSABLE:
            nb_admis = nb_admis + 1
    return round(nb_admis / len(liste_notes) * 100, 1)


def notes_par_matiere(matiere_cible):
    """
    Extrait les noms et notes d'une matiere donnee depuis les listes globales.
    Retourne deux listes : (noms_filtres, notes_filtrees)
    """
    noms_filtres  = []
    notes_filtres = []
    for i in range(len(matieres)):
        if matieres[i] == matiere_cible:
            noms_filtres.append(noms_eleves[i])
            notes_filtres.append(notes[i])
    return noms_filtres, notes_filtres


def moyenne_par_matiere(matieres_uniques):
    """Retourne un dictionnaire {matiere: moyenne} pour toutes les matieres evaluees."""
    moyennes = {}
    for mat in matieres_uniques:
        _, notes_mat = notes_par_matiere(mat)
        moyennes[mat] = calculer_moyenne(notes_mat)
    return moyennes


def matieres_uniques():
    """Retourne le set des matieres evaluees sans doublon."""
    uniques = set()
    for mat in matieres:
        uniques.add(mat)
    return uniques


def noms_uniques():
    """Retourne le set des noms d'eleves sans doublon."""
    uniques = set()
    for nom in noms_eleves:
        uniques.add(nom)
    return uniques

# ============================================================
# SECTION 4 : AFFICHAGE DES RAPPORTS
# ============================================================

def afficher_rapport_matiere(matiere):
    """Affiche le rapport detaille pour une matiere donnee."""

    # Extraire les donnees de cette matiere uniquement
    liste_noms, liste_notes = notes_par_matiere(matiere)

    # Calculs
    moyenne       = calculer_moyenne(liste_notes)
    eleve_min, eleve_max = note_min_max(liste_noms, liste_notes)
    compteurs     = compteur_mentions(liste_notes)
    en_diff       = eleves_en_difficulte(liste_noms, liste_notes)
    top3          = classement_top3(liste_noms, liste_notes)
    taux          = taux_reussite(liste_notes)
    mention       = attribuer_mention(moyenne)

    print()
    print('=' * 60)
    print(f'   RAPPORT - {matiere.upper()}')
    print(f'   {NOM_CLASSE} | {NOM_ECOLE}')
    print('=' * 60)

    print(f'\n  Nombre d eleves  : {len(liste_notes)}')
    print(f'  Moyenne classe   : {moyenne} / 20  ({mention})')
    print(f'  Taux de reussite : {taux}%')
    print(f'  Meilleur eleve   : {eleve_max[0]} ({eleve_max[1]} / 20)')
    print(f'  Plus en difficulte : {eleve_min[0]} ({eleve_min[1]} / 20)')

    # Distribution des mentions
    print()
    print('-' * 60)
    print('  DISTRIBUTION DES MENTIONS')
    print('-' * 60)
    for mention_nom, nb in compteurs.items():
        pct   = round(nb / len(liste_notes) * 100, 1)
        barre = '#' * nb
        print(f'  {mention_nom:<12} : {nb:>3} eleve(s)  ({pct}%)  {barre}')

    # Top 3
    print()
    print('-' * 60)
    print('  TABLEAU - TOP 3')
    print('-' * 60)
    medailles = ['Or    ', 'Argent', 'Bronze']
    for i, (nom, note) in enumerate(top3):
        print(f'  {medailles[i]} : {nom:<25} - {note} / 20  ({attribuer_mention(note)})')

    # Eleves en difficulte
    print()
    print('-' * 60)
    if len(en_diff) == 0:
        print('  Aucun eleve en difficulte.')
    else:
        print(f'  ELEVES EN DIFFICULTE - {len(en_diff)} eleve(s) < 10/20')
        print('-' * 60)
        for nom, note in en_diff:
            print(f'  !! {nom:<25} : {note} / 20 - Soutien recommande')

    # Classement complet
    print()
    print('-' * 60)
    print('  CLASSEMENT COMPLET')
    print('-' * 60)
    paires_triees = sorted(
        [(liste_noms[i], liste_notes[i]) for i in range(len(liste_noms))],
        key=lambda x: x[1],
        reverse=True
    )
    for rang, (nom, note) in enumerate(paires_triees, 1):
        print(f'  {rang:>2}. {nom:<25} : {note:>5} / 20  - {attribuer_mention(note)}')

    print()
    print('=' * 60)


def afficher_bilan_general(matieres_list):
    """
    Affiche le bilan comparatif de toutes les matieres
    et le classement general des eleves.
    """
    moyennes = moyenne_par_matiere(matieres_list)

    print()
    print('=' * 60)
    print('   BILAN GENERAL - TOUTES MATIERES')
    print(f'   {NOM_CLASSE} | {NOM_ECOLE}')
    print('=' * 60)

    # Comparaison des moyennes par matiere
    print()
    print('  MOYENNES PAR MATIERE')
    print('-' * 60)
    for mat, moy in sorted(moyennes.items(), key=lambda x: x[1], reverse=True):
        barre = '#' * int(moy)
        print(f'  {mat:<20} : {moy:>5} / 20  ({attribuer_mention(moy)})  {barre}')

    # Matiere la plus forte et la plus faible
    mat_forte  = max(moyennes, key=lambda x: moyennes[x])
    mat_faible = min(moyennes, key=lambda x: moyennes[x])
    print()
    print(f'  >> Matiere la plus forte  : {mat_forte} ({moyennes[mat_forte]} / 20)')
    print(f'  >> Matiere la plus faible : {mat_faible} ({moyennes[mat_faible]} / 20)')

    # Moyenne generale de chaque eleve (sur toutes les matieres)
    print()
    print('-' * 60)
    print('  CLASSEMENT GENERAL DES ELEVES (moyenne toutes matieres)')
    print('-' * 60)

    # On calcule la moyenne generale par eleve
    eleves_list = list(noms_uniques())
    moyennes_eleves = []

    for eleve in eleves_list:
        notes_eleve = []
        for i in range(len(noms_eleves)):
            if noms_eleves[i] == eleve:
                notes_eleve.append(notes[i])
        moy_eleve = calculer_moyenne(notes_eleve)
        moyennes_eleves.append((eleve, moy_eleve))

    moyennes_eleves_triees = sorted(moyennes_eleves, key=lambda x: x[1], reverse=True)

    for rang, (nom, moy) in enumerate(moyennes_eleves_triees, 1):
        print(f'  {rang:>2}. {nom:<25} : {moy:>5} / 20  - {attribuer_mention(moy)}')

    print()
    print('=' * 60)

# ============================================================
# SECTION 5 : PROGRAMME PRINCIPAL
# ============================================================

if __name__ == '__main__':
    print('=' * 60)
    print('   SYSTEME D ANALYSE DES NOTES - MULTI-MATIERES')
    print(f'   {NOM_CLASSE} - {NOM_ECOLE}')
    print('   Akieni Academy - Semaine 6')
    print('=' * 60)

    # Nombre d'eleves
    try:
        nb_eleves = int(input('\nNombre d eleves dans la classe : '))
        if nb_eleves <= 0:
            nb_eleves = 1
    except ValueError:
        nb_eleves = 10
        print('Valeur invalide - 10 eleves par defaut')

    # Nombre de matieres
    try:
        nb_matieres = int(input('Nombre de matieres a evaluer : '))
        if nb_matieres <= 0:
            nb_matieres = 1
    except ValueError:
        nb_matieres = 1
        print('Valeur invalide - 1 matiere par defaut')

    # Saisie matiere selon le nombre de matiere
    for m in range(1, nb_matieres + 1):
        print()
        matiere = input(f'Nom de la matiere {m} : ').strip()
        if matiere == '':
            matiere = f'Matiere {m}'

        saisir_notes(nb_eleves, matiere)
        afficher_rapport_matiere(matiere)

    # Bilan general si plusieurs matieres
    if nb_matieres > 1:
        afficher_bilan_general(matieres_uniques())
