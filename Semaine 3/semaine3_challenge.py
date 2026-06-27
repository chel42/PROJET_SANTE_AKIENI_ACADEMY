# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Challenge : Tableau de Bord 5 Hopitaux
# Notions S2 : variables, operateurs, f-strings
# Notions S3 : if / elif / else, conditions composees and / or
# ============================================================

# ============================================================
# SECTION 1 : DONNEES DES 5 HOPITAUX
# ============================================================

# Hopital 1 — CHU Brazzaville
h1_nom            = 'CHU Brazzaville'
h1_lits_total     = 320
h1_lits_occupes   = 298
h1_nb_medecins    = 47
h1_nb_ruptures    = 2   
h1_nb_alertes     = 2   

# Hopital 2 — Hopital Pointe-Noire
h2_nom            = 'Hopital Pointe-Noire'
h2_lits_total     = 180
h2_lits_occupes   = 143
h2_nb_medecins    = 22
h2_nb_ruptures    = 0
h2_nb_alertes     = 1   

# Hopital 3 — Hopital Dolisie
h3_nom            = 'Hopital Dolisie'
h3_lits_total     = 95
h3_lits_occupes   = 91
h3_nb_medecins    = 8
h3_nb_ruptures    = 1   
h3_nb_alertes     = 2   

# Hopital 4 — Hopital Owando
h4_nom            = 'Hopital Owando'
h4_lits_total     = 45
h4_lits_occupes   = 32
h4_nb_medecins    = 3
h4_nb_ruptures    = 3  
h4_nb_alertes     = 0

# Hopital 5 — CMS Impfondo
h5_nom            = 'CMS Impfondo'
h5_lits_total     = 20
h5_lits_occupes   = 19
h5_nb_medecins    = 1
h5_nb_ruptures    = 2   
h5_nb_alertes     = 1  

# ============================================================
# SECTION 2 : CALCUL DES TAUX D'OCCUPATION 
# ============================================================

h1_taux_occ = round(h1_lits_occupes / h1_lits_total * 100, 1)
h2_taux_occ = round(h2_lits_occupes / h2_lits_total * 100, 1)
h3_taux_occ = round(h3_lits_occupes / h3_lits_total * 100, 1)
h4_taux_occ = round(h4_lits_occupes / h4_lits_total * 100, 1)
h5_taux_occ = round(h5_lits_occupes / h5_lits_total * 100, 1)

# ============================================================
# SECTION 3 : NIVEAU D'OCCUPATION (S3)
# ============================================================

# Hopital 1
if h1_taux_occ > 95:
    h1_niveau_occ = 'CRI'
elif h1_taux_occ > 85:
    h1_niveau_occ = 'ALT'
elif h1_taux_occ > 70:
    h1_niveau_occ = 'OK '
else:
    h1_niveau_occ = 'BAS'

# Hopital 2
if h2_taux_occ > 95:
    h2_niveau_occ = 'CRI'
elif h2_taux_occ > 85:
    h2_niveau_occ = 'ALT'
elif h2_taux_occ > 70:
    h2_niveau_occ = 'OK '
else:
    h2_niveau_occ = 'BAS'

# Hopital 3
if h3_taux_occ > 95:
    h3_niveau_occ = 'CRI'
elif h3_taux_occ > 85:
    h3_niveau_occ = 'ALT'
elif h3_taux_occ > 70:
    h3_niveau_occ = 'OK '
else:
    h3_niveau_occ = 'BAS'

# Hopital 4
if h4_taux_occ > 95:
    h4_niveau_occ = 'CRI'
elif h4_taux_occ > 85:
    h4_niveau_occ = 'ALT'
elif h4_taux_occ > 70:
    h4_niveau_occ = 'OK '
else:
    h4_niveau_occ = 'BAS'

# Hopital 5
if h5_taux_occ > 95:
    h5_niveau_occ = 'CRI'
elif h5_taux_occ > 85:
    h5_niveau_occ = 'ALT'
elif h5_taux_occ > 70:
    h5_niveau_occ = 'OK '
else:
    h5_niveau_occ = 'BAS'

# ============================================================
# SECTION 4 : NIVEAU D'ALERTE GLOBAL (S3)
# Regles :
#   CRITIQUE     : ruptures >= 2 OU taux > 95%
#   PREOCCUPANT  : ruptures >= 1 OU taux > 85% OU (alertes >= 2 ET medecins < 5)
#   SATISFAISANT : toutes conditions normales
# ============================================================

# Hopital 1
if h1_nb_ruptures >= 2 or h1_taux_occ > 95:
    h1_niveau_global = '[CRITIQUE]'
elif h1_nb_ruptures >= 1 or h1_taux_occ > 85 or (h1_nb_alertes >= 2 and h1_nb_medecins < 5):
    h1_niveau_global = '[PREOCCUPANT]'
else:
    h1_niveau_global = '[SATISFAISANT]'

# Hopital 2
if h2_nb_ruptures >= 2 or h2_taux_occ > 95:
    h2_niveau_global = '[CRITIQUE]'
elif h2_nb_ruptures >= 1 or h2_taux_occ > 85 or (h2_nb_alertes >= 2 and h2_nb_medecins < 5):
    h2_niveau_global = '[PREOCCUPANT]'
else:
    h2_niveau_global = '[SATISFAISANT]'

# Hopital 3
if h3_nb_ruptures >= 2 or h3_taux_occ > 95:
    h3_niveau_global = '[CRITIQUE]'
elif h3_nb_ruptures >= 1 or h3_taux_occ > 85 or (h3_nb_alertes >= 2 and h3_nb_medecins < 5):
    h3_niveau_global = '[PREOCCUPANT]'
else:
    h3_niveau_global = '[SATISFAISANT]'

# Hopital 4
if h4_nb_ruptures >= 2 or h4_taux_occ > 95:
    h4_niveau_global = '[CRITIQUE]'
elif h4_nb_ruptures >= 1 or h4_taux_occ > 85 or (h4_nb_alertes >= 2 and h4_nb_medecins < 5):
    h4_niveau_global = '[PREOCCUPANT]'
else:
    h4_niveau_global = '[SATISFAISANT]'

# Hopital 5
if h5_nb_ruptures >= 2 or h5_taux_occ > 95:
    h5_niveau_global = '[CRITIQUE]'
elif h5_nb_ruptures >= 1 or h5_taux_occ > 85 or (h5_nb_alertes >= 2 and h5_nb_medecins < 5):
    h5_niveau_global = '[PREOCCUPANT]'
else:
    h5_niveau_global = '[SATISFAISANT]'

# ============================================================
# SECTION 5 : COMPTEURS NATIONAUX
# ============================================================

nb_hopitaux_critiques = 0

if h1_niveau_global == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h2_niveau_global == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h3_niveau_global == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h4_niveau_global == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1
if h5_niveau_global == '[CRITIQUE]':
    nb_hopitaux_critiques = nb_hopitaux_critiques + 1

# Total des ruptures de stock a l'echelle nationale 
nb_ruptures_national = h1_nb_ruptures + h2_nb_ruptures + h3_nb_ruptures + h4_nb_ruptures + h5_nb_ruptures

# Cout estime des commandes urgentes 
# cout unitaire moyen d'une commande express : 450 000 FCFA
cout_commande_express = 450_000.0
cout_total_commandes  = nb_ruptures_national * cout_commande_express

# ============================================================
# SECTION 6 : AFFICHAGE DU TABLEAU DE BORD
# ============================================================

print('=' * 64)
print('  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print('  Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 64)
print(f'  {"HOPITAL":<22} {"OCCUPATION":<14} {"ALERTES":<10} {"NIVEAU GLOBAL"}')
print('-' * 64)

print(f'  {h1_nom:<22} {h1_taux_occ}% [{h1_niveau_occ}]    {h1_nb_ruptures}R + {h1_nb_alertes}A    {h1_niveau_global}')
print(f'  {h2_nom:<22} {h2_taux_occ}% [{h2_niveau_occ}]    {h2_nb_ruptures}R + {h2_nb_alertes}A    {h2_niveau_global}')
print(f'  {h3_nom:<22} {h3_taux_occ}% [{h3_niveau_occ}]    {h3_nb_ruptures}R + {h3_nb_alertes}A    {h3_niveau_global}')
print(f'  {h4_nom:<22} {h4_taux_occ}% [{h4_niveau_occ}]    {h4_nb_ruptures}R + {h4_nb_alertes}A    {h4_niveau_global}')
print(f'  {h5_nom:<22} {h5_taux_occ}% [{h5_niveau_occ}]    {h5_nb_ruptures}R + {h5_nb_alertes}A    {h5_niveau_global}')

print('-' * 64)
print(f'  {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE')
print(f'  {nb_ruptures_national} ruptures de stock identifiees a l echelle nationale')

# Recommandation conditionnelle selon le nombre de critiques
if nb_hopitaux_critiques >= 4:
    print(f'  RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA')
elif nb_hopitaux_critiques >= 2:
    print(f'  RECOMMANDATION : Declencher les commandes urgentes dans les hopitaux critiques')
else:
    print(f'  RECOMMANDATION : Surveillance renforcee des hopitaux identifies')

print('=' * 64)

# BONUS : cout des commandes urgentes
print(f'\n  BONUS — ANALYSE FINANCIERE URGENCE')
print(f'  Ruptures nationales      : {nb_ruptures_national} medicaments')
print(f'  Cout commande express    : {cout_commande_express:,.0f} FCFA / commande'.replace(',', ' '))
print(f'  Cout total estime        : {cout_total_commandes:,.0f} FCFA'.replace(',', ' '))
print('=' * 64)
