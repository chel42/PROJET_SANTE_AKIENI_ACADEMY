# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Challenge : Rapport 3 Hopitaux du Pool
# ============================================================


# --- SECTION 1 : DONNEES DES 3 HOPITAUX ---

# TODO : Déclaration des variables pour Hopital District Kinkala 
#
h1_nom               = 'Hopital District Kinkala'
h1_budget_fcfa       = 12_500_000.0   # Budget trimestriel en FCFA (float)
h1_nb_consultations  = 1847            # Consultations externes (int)
h1_nb_hospit         = 312             # Hospitalisations (int)
h1_nb_deces          = 8              # Deces hospitaliers (int)
h1_nb_lits_total     = 45             # Lits totaux (int)
h1_nb_lits_occupes   = 41             # Lits occupes (int)
h1_nb_medecins       = 3              # Medecins permanents (int)
h1_population        = 85_000         # Population desservie (int)

# TODO : Déclaration des variables pour CMS de Vindza 
#
h2_nom               = 'CMS de Vindza'
h2_budget_fcfa       = 6_800_000.0
h2_nb_consultations  = 923
h2_nb_hospit         = 87
h2_nb_deces          = 2
h2_nb_lits_total     = 20
h2_nb_lits_occupes   = 14
h2_nb_medecins       = 1
h2_population        = 42_000

# TODO : Déclaration des variables pour Hopital de Kindamba 
#
h3_nom               = 'Hopital de Kindamba'
h3_budget_fcfa       = 9_200_000.0
h3_nb_consultations  = 1234
h3_nb_hospit         = 201
h3_nb_deces          = 11
h3_nb_lits_total     = 35
h3_nb_lits_occupes   = 33
h3_nb_medecins       = 2
h3_population        = 67_000

# --- SECTION 2 : CALCULS DES KPIs POUR CHAQUE HOPITAL ---

# TODO : Calculs KPIs Hopital 1
#
h1_cout_moyen       = round(h1_budget_fcfa / (h1_nb_consultations + h1_nb_hospit), 2)
h1_taux_occupation  = round(h1_nb_lits_occupes / h1_nb_lits_total * 100, 2)
h1_densite_medicale = round((h1_nb_medecins / h1_population) * 1000, 2)
h1_taux_mortalite   = round((h1_nb_deces / h1_nb_hospit) * 100, 2)

# TODO : Calculs KPIs Hopital 2
#
h2_cout_moyen       = round(h2_budget_fcfa / (h2_nb_consultations + h2_nb_hospit), 2)
h2_taux_occupation  = round(h2_nb_lits_occupes / h2_nb_lits_total * 100, 2)
h2_densite_medicale = round((h2_nb_medecins / h2_population) * 1000, 2)
h2_taux_mortalite   = round((h2_nb_deces / h2_nb_hospit) * 100, 2)

# TODO : Calculs KPIs Hopital 3
#
h3_cout_moyen       = round(h3_budget_fcfa / (h3_nb_consultations + h3_nb_hospit), 2)
h3_taux_occupation  = round(h3_nb_lits_occupes / h3_nb_lits_total * 100, 2)
h3_densite_medicale = round((h3_nb_medecins / h3_population) * 1000, 2)
h3_taux_mortalite   = round((h3_nb_deces / h3_nb_hospit) * 100, 2)


# --- SECTION 3 : IDENTIFICATION DES HOPITAUX CRITIQUES ---

# TODO : Un hopital est critique si taux_mortalite > 2% OU densite < 0.05
#
h1_critique = (h1_taux_mortalite > 2.0) or (h1_densite_medicale < 0.05)
if h1_critique == True:
    statut_h1 = 'CRITIQUE'
else:
    statut_h1 = 'NORMAL'

h2_critique = (h2_taux_mortalite > 2.0) or (h2_densite_medicale < 0.05)
if h2_critique == True:
    statut_h2 = 'CRITIQUE'
else:
    statut_h2 = 'NORMAL'

h3_critique = (h3_taux_mortalite > 2.0) or (h3_densite_medicale < 0.05)
if h3_critique == True:
    statut_h3 = 'CRITIQUE'
else:
    statut_h3 = 'NORMAL'

# --- SECTION 4 : BONUS — Budget suffisant pour 5 medecins chacun ---

cout_medecin_trim     = 1_200_000.0   
budget_total_3hopitaux = h1_budget_fcfa + h2_budget_fcfa + h3_budget_fcfa

# Chaque hopital doit avoir 5 medecins
medecins_actuels_total = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins
medecins_cibles_total  = 5 * 3  # 5 medecins par hopital x 3 hopitaux
medecins_a_recruter    = medecins_cibles_total - medecins_actuels_total
cout_recrutement_total = medecins_a_recruter * cout_medecin_trim

budget_suffisant = budget_total_3hopitaux >= (budget_total_3hopitaux - cout_recrutement_total + cout_recrutement_total)
budget_apres_recrutement = budget_total_3hopitaux - cout_recrutement_total

# --- SECTION 5 : RAPPORT CONSOLIDE ---

print()
print('=' * 65)
print('  RAPPORT COMPARATIF — 3 HOPITAUX DU DEPARTEMENT DU POOL')
print('  Date : 08 janvier 2026  |  Demandeur : Dr. ELENGA Pascal')
print('=' * 65)

# Hopital 1
print(f'\n  {h1_nom}')
print(f'  {"-" * 40}')
print(f'  Cout moyen / patient  : {h1_cout_moyen:,.0f} FCFA'.replace(',', ' '))
print(f'  Taux occupation       : {h1_taux_occupation}%')
print(f'  Densite medicale      : {h1_densite_medicale} med. / 1000 hab')
print(f'  Taux mortalite        : {h1_taux_mortalite}%')
print(f'  Statut                : {statut_h1}')

# Hopital 2
print(f'\n  {h2_nom}')
print(f'  {"-" * 40}')
print(f'  Cout moyen / patient  : {h2_cout_moyen:,.0f} FCFA'.replace(',', ' '))
print(f'  Taux occupation       : {h2_taux_occupation}%')
print(f'  Densite medicale      : {h2_densite_medicale} med. / 1000 hab')
print(f'  Taux mortalite        : {h2_taux_mortalite}%')
print(f'  Statut                : {statut_h2}')

# Hopital 3
print(f'\n  {h3_nom}')
print(f'  {"-" * 40}')
print(f'  Cout moyen / patient  : {h3_cout_moyen:,.0f} FCFA'.replace(',', ' '))
print(f'  Taux occupation       : {h3_taux_occupation}%')
print(f'  Densite medicale      : {h3_densite_medicale} med. / 1000 hab')
print(f'  Taux mortalite        : {h3_taux_mortalite}%')
print(f'  Statut                : {statut_h3}')

# Alertes critiques
print(f'\n{"=" * 65}')
print(f'  ALERTES CRITIQUES')
print(f'{"=" * 65}')
if h1_critique:
    print(f'  !! {h1_nom} : mortalite={h1_taux_mortalite}% / densite={h1_densite_medicale}')
if h2_critique:
    print(f'  !! {h2_nom} : mortalite={h2_taux_mortalite}% / densite={h2_densite_medicale}')
if h3_critique:
    print(f'  !! {h3_nom} : mortalite={h3_taux_mortalite}% / densite={h3_densite_medicale}')
if not h1_critique and not h2_critique and not h3_critique:
    print(f'  Aucun hopital en situation critique.')

# Bonus budget
print(f'\n{"=" * 65}')
print(f'  BONUS — ANALYSE BUDGET RECRUTEMENT (objectif : 5 med. / hopital)')
print(f'{"=" * 65}')
print(f'  Budget total 3 hopitaux  : {budget_total_3hopitaux:,.0f} FCFA'.replace(',', ' '))
print(f'  Medecins actuels         : {medecins_actuels_total} medecins')
print(f'  Medecins a recruter      : {medecins_a_recruter} medecins')
print(f'  Cout recrutement total   : {cout_recrutement_total:,.0f} FCFA'.replace(',', ' '))
if budget_apres_recrutement >= 0:
    print(f'  Budget restant apres recrutement : {budget_apres_recrutement:,.0f} FCFA — FAISABLE'.replace(',', ' '))
else:
    print(f'  Deficit : {abs(budget_apres_recrutement):,.0f} FCFA — NON FAISABLE'.replace(',', ' '))
print('=' * 65)
