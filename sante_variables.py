# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# ============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========

TAUX_EUR_FCFA              = 655.957   # Taux de change fixe Zone CFA
TAUX_USD_FCFA              = 600.0     # Taux approximatif 2025
SEUIL_OMS_DENSITE_MEDICALE = 2.3       # Medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN= 95.0      # Pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE     = 2.0       # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS  = 30        # Jours minimum de stock

DEPARTEMENTS_CONGO = [                 # 12 departements officiels du Congo
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]

# === SECTION B : VARIABLES DES 5 HOPITAUX ===================

# Hopital 1 — CHU de Brazzaville
h1_nom             = 'CHU de Brazzaville'
h1_ville           = 'Brazzaville'
h1_departement     = 'Brazzaville'
h1_type            = 'CHU'
h1_nb_lits         = 320
h1_nb_lits_occupes = 284
h1_nb_medecins     = 47
h1_nb_infirmiers   = 123
h1_population_zone = 1_800_000
h1_budget_fcfa     = 450_000_000.0  

# Hopital 2 — Hopital General de Pointe-Noire
h2_nom             = 'Hopital General de Pointe-Noire'
h2_ville           = 'Pointe-Noire'
h2_departement     = 'Kouilou'
h2_type            = 'Hopital General'
h2_nb_lits         = 180
h2_nb_lits_occupes = 143
h2_nb_medecins     = 22
h2_nb_infirmiers   = 58
h2_population_zone = 128_000
h2_budget_fcfa     = 87_450_000.0

# Hopital 3 — Hopital de Dolisie
h3_nom             = 'Hopital de Dolisie'
h3_ville           = 'Dolisie'
h3_departement     = 'Niari'
h3_type            = 'Hopital Departemental'
h3_nb_lits         = 120
h3_nb_lits_occupes = 98
h3_nb_medecins     = 15
h3_nb_infirmiers   = 42
h3_population_zone = 95_000
h3_budget_fcfa     = 62_000_000.0

# Hopital 4 — Hopital de District Owando
h4_nom             = 'Hopital de District Owando'
h4_ville           = 'Owando'
h4_departement     = 'Cuvette'
h4_type            = 'Hopital de District'
h4_nb_lits         = 60
h4_nb_lits_occupes = 44
h4_nb_medecins     = 7
h4_nb_infirmiers   = 20
h4_population_zone = 52_000
h4_budget_fcfa     = 38_000_000.0

# Hopital 5 — Centre de Sante de Impfondo
h5_nom             = 'Centre de Sante de Impfondo'
h5_ville           = 'Impfondo'
h5_departement     = 'Likouala'
h5_type            = 'Centre de Sante'
h5_nb_lits         = 30
h5_nb_lits_occupes = 19
h5_nb_medecins     = 3
h5_nb_infirmiers   = 9
h5_population_zone = 38_000
h5_budget_fcfa     = 18_500_000.0

# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================

# Medicament 1 — Artemether-Lumefantrine 
med1_nom           = 'Artemether-Lumefantrine'
med1_quantite      = 4850      
med1_seuil_rupture = 500       
med1_cout_unitaire = 3500.0    

# Medicament 2 — Amoxicilline 500mg
med2_nom           = 'Amoxicilline 500mg'
med2_quantite      = 12000
med2_seuil_rupture = 1000
med2_cout_unitaire = 450.0

# Medicament 3 — Paracetamol 500mg
med3_nom           = 'Paracetamol 500mg'
med3_quantite      = 25000
med3_seuil_rupture = 2000
med3_cout_unitaire = 75.0

# Medicament 4 — SRO 
med4_nom           = 'SRO - Sels de Rehydratation Orale'
med4_quantite      = 8200
med4_seuil_rupture = 800
med4_cout_unitaire = 250.0

# Medicament 5 — Vaccin Antipaludeen 
med5_nom           = 'Vaccin Antipaludeen RTS,S'
med5_quantite      = 620
med5_seuil_rupture = 100
med5_cout_unitaire = 12000.0

# === SECTION D : CALCULS D'INITIALISATION ===================

# Total medecins et population sur les 5 hopitaux
total_medecins  = h1_nb_medecins + h2_nb_medecins + h3_nb_medecins + h4_nb_medecins + h5_nb_medecins
total_population = h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone

# Densite medicale nationale (sur les zones couvertes)
densite_medicale_nationale = round((total_medecins / total_population) * 1000, 2)

# Taux d'occupation moyen des 5 hopitaux
total_lits       = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_lits_occ   = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_occupation_moyen = round(total_lits_occ / total_lits * 100, 1)

# Valeur totale du stock de medicaments
valeur_stock_total = (
    med1_quantite * med1_cout_unitaire +
    med2_quantite * med2_cout_unitaire +
    med3_quantite * med3_cout_unitaire +
    med4_quantite * med4_cout_unitaire +
    med5_quantite * med5_cout_unitaire
)

# Budget total annuel des 5 hopitaux
budget_total_fcfa = h1_budget_fcfa + h2_budget_fcfa + h3_budget_fcfa + h4_budget_fcfa + h5_budget_fcfa

# === SECTION E : RAPPORT D'INVENTAIRE =======================

print('=' * 65)
print('  MODULE FONDATEUR — SYSTEME DE SANTE CONGO')
print('  Akieni Academy | Version 2026 | Projet Fil Rouge S1')
print('=' * 65)

print(f'\n  PERIMETRE : {len(DEPARTEMENTS_CONGO)} departements du Congo')
print(f'  Hopitaux repertories : 5 etablissements')

print(f'\n{"=" * 65}')
print(f'  KPIs GLOBAUX INITIAUX')
print(f'{"=" * 65}')
print(f'  Medecins total       : {total_medecins}')
print(f'  Population couverte  : {total_population:_} hab'.replace('_', ' '))
print(f'  Densite medicale     : {densite_medicale_nationale} med. / 1000 hab  [OMS : >= {SEUIL_OMS_DENSITE_MEDICALE}]')
print(f'  Lits totaux          : {total_lits}')
print(f'  Lits occupes         : {total_lits_occ}')
print(f'  Taux occupation moy. : {taux_occupation_moyen}%')
print(f'  Budget total annuel  : {budget_total_fcfa:_.0f} FCFA'.replace('_', ' '))

print(f'\n{"=" * 65}')
print(f'  INVENTAIRE MEDICAMENTS')
print(f'{"=" * 65}')

# Affichage de chaque medicament avec alerte si rupture proche
medicaments = [
    (med1_nom, med1_quantite, med1_seuil_rupture, med1_cout_unitaire),
    (med2_nom, med2_quantite, med2_seuil_rupture, med2_cout_unitaire),
    (med3_nom, med3_quantite, med3_seuil_rupture, med3_cout_unitaire),
    (med4_nom, med4_quantite, med4_seuil_rupture, med4_cout_unitaire),
    (med5_nom, med5_quantite, med5_seuil_rupture, med5_cout_unitaire),
]

for nom, qte, seuil, cout in medicaments:
    valeur = qte * cout
    alerte = ' !! RUPTURE PROCHE' if qte <= seuil * 1.5 else ''
    print(f'  {nom}')
    print(f'    Stock : {qte} unites | Seuil rupture : {seuil} | Valeur : {valeur:,.0f} FCFA{alerte}'.replace(',', ' '))

print(f'\n  Valeur totale du stock : {valeur_stock_total:,.0f} FCFA'.replace(',', ' '))

# Alerte densite medicale
print(f'\n{"=" * 65}')
if densite_medicale_nationale < SEUIL_OMS_DENSITE_MEDICALE:
    print(f'  !! ALERTE : Densite medicale sous la norme OMS')
    print(f'     Actuelle : {densite_medicale_nationale} — Norme : {SEUIL_OMS_DENSITE_MEDICALE} medecins / 1000 hab')
print(f'{"=" * 65}')
print(f'  Module charge avec succes. Pret pour Semaine 3.')
print(f'{"=" * 65}')

# ============================================================
# === SECTION F : CLASSIFICATION STATUT STOCKS (NEW S3) ======
# Regles PNA Congo — if / elif / else
# On utilise les constantes de SECTION A, pas de valeurs hardcodees
# ============================================================

# Seuils calcules a partir de la constante SEUIL_RUPTURE_STOCK_JOURS

# --- Medicament 1 : Artemether-Lumefantrine ---
if med1_quantite <= med1_seuil_rupture:
    med1_statut  = 'RUPTURE CRITIQUE'
    med1_couleur = '[ROUGE]'
elif med1_quantite <= med1_seuil_rupture * 1.5:
    med1_statut  = 'ALERTE STOCK'
    med1_couleur = '[ORANGE]'
elif med1_quantite <= med1_seuil_rupture * 2.0:
    med1_statut  = 'STOCK LIMITE'
    med1_couleur = '[JAUNE]'
else:
    med1_statut  = 'STOCK NORMAL'
    med1_couleur = '[VERT]'

# --- Medicament 2 : Amoxicilline 500mg ---
if med2_quantite <= med2_seuil_rupture:
    med2_statut  = 'RUPTURE CRITIQUE'
    med2_couleur = '[ROUGE]'
elif med2_quantite <= med2_seuil_rupture * 1.5:
    med2_statut  = 'ALERTE STOCK'
    med2_couleur = '[ORANGE]'
elif med2_quantite <= med2_seuil_rupture * 2.0:
    med2_statut  = 'STOCK LIMITE'
    med2_couleur = '[JAUNE]'
else:
    med2_statut  = 'STOCK NORMAL'
    med2_couleur = '[VERT]'

# --- Medicament 3 : Paracetamol 500mg ---
if med3_quantite <= med3_seuil_rupture:
    med3_statut  = 'RUPTURE CRITIQUE'
    med3_couleur = '[ROUGE]'
elif med3_quantite <= med3_seuil_rupture * 1.5:
    med3_statut  = 'ALERTE STOCK'
    med3_couleur = '[ORANGE]'
elif med3_quantite <= med3_seuil_rupture * 2.0:
    med3_statut  = 'STOCK LIMITE'
    med3_couleur = '[JAUNE]'
else:
    med3_statut  = 'STOCK NORMAL'
    med3_couleur = '[VERT]'

# --- Medicament 4 : SRO ---
if med4_quantite <= med4_seuil_rupture:
    med4_statut  = 'RUPTURE CRITIQUE'
    med4_couleur = '[ROUGE]'
elif med4_quantite <= med4_seuil_rupture * 1.5:
    med4_statut  = 'ALERTE STOCK'
    med4_couleur = '[ORANGE]'
elif med4_quantite <= med4_seuil_rupture * 2.0:
    med4_statut  = 'STOCK LIMITE'
    med4_couleur = '[JAUNE]'
else:
    med4_statut  = 'STOCK NORMAL'
    med4_couleur = '[VERT]'

# --- Medicament 5 : Vaccin Antipaludeen ---
if med5_quantite <= med5_seuil_rupture:
    med5_statut  = 'RUPTURE CRITIQUE'
    med5_couleur = '[ROUGE]'
elif med5_quantite <= med5_seuil_rupture * 1.5:
    med5_statut  = 'ALERTE STOCK'
    med5_couleur = '[ORANGE]'
elif med5_quantite <= med5_seuil_rupture * 2.0:
    med5_statut  = 'STOCK LIMITE'
    med5_couleur = '[JAUNE]'
else:
    med5_statut  = 'STOCK NORMAL'
    med5_couleur = '[VERT]'

# Comptage des alertes medicaments
nb_ruptures_meds = 0
nb_alertes_meds  = 0

if med1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_meds = nb_ruptures_meds + 1
elif med1_statut == 'ALERTE STOCK':
    nb_alertes_meds = nb_alertes_meds + 1

if med2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_meds = nb_ruptures_meds + 1
elif med2_statut == 'ALERTE STOCK':
    nb_alertes_meds = nb_alertes_meds + 1

if med3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_meds = nb_ruptures_meds + 1
elif med3_statut == 'ALERTE STOCK':
    nb_alertes_meds = nb_alertes_meds + 1

if med4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_meds = nb_ruptures_meds + 1
elif med4_statut == 'ALERTE STOCK':
    nb_alertes_meds = nb_alertes_meds + 1

if med5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_meds = nb_ruptures_meds + 1
elif med5_statut == 'ALERTE STOCK':
    nb_alertes_meds = nb_alertes_meds + 1

# ============================================================
# === SECTION G : CLASSIFICATION OCCUPATION HOPITAUX (NEW S3)
# Regles DSS Congo : > 95% CRITIQUE / > 85% ELEVE / > 70% OPTIMAL / sinon SOUS-UTILISE
# ============================================================

# Calcul taux d'occupation de chaque hopital (S2)
h1_taux_occ = round(h1_nb_lits_occupes / h1_nb_lits * 100, 1)
h2_taux_occ = round(h2_nb_lits_occupes / h2_nb_lits * 100, 1)
h3_taux_occ = round(h3_nb_lits_occupes / h3_nb_lits * 100, 1)
h4_taux_occ = round(h4_nb_lits_occupes / h4_nb_lits * 100, 1)
h5_taux_occ = round(h5_nb_lits_occupes / h5_nb_lits * 100, 1)

# Hopital 1
if h1_taux_occ > 95:
    h1_niveau_occ = 'CRITIQUE — saturation, transferts a organiser'
elif h1_taux_occ > 85:
    h1_niveau_occ = 'ELEVE — capacite limite, renforcement prevu'
elif h1_taux_occ > 70:
    h1_niveau_occ = 'OPTIMAL'
else:
    h1_niveau_occ = 'SOUS-UTILISATION'

# Hopital 2
if h2_taux_occ > 95:
    h2_niveau_occ = 'CRITIQUE — saturation, transferts a organiser'
elif h2_taux_occ > 85:
    h2_niveau_occ = 'ELEVE — capacite limite, renforcement prevu'
elif h2_taux_occ > 70:
    h2_niveau_occ = 'OPTIMAL'
else:
    h2_niveau_occ = 'SOUS-UTILISATION'

# Hopital 3
if h3_taux_occ > 95:
    h3_niveau_occ = 'CRITIQUE — saturation, transferts a organiser'
elif h3_taux_occ > 85:
    h3_niveau_occ = 'ELEVE — capacite limite, renforcement prevu'
elif h3_taux_occ > 70:
    h3_niveau_occ = 'OPTIMAL'
else:
    h3_niveau_occ = 'SOUS-UTILISATION'

# Hopital 4
if h4_taux_occ > 95:
    h4_niveau_occ = 'CRITIQUE — saturation, transferts a organiser'
elif h4_taux_occ > 85:
    h4_niveau_occ = 'ELEVE — capacite limite, renforcement prevu'
elif h4_taux_occ > 70:
    h4_niveau_occ = 'OPTIMAL'
else:
    h4_niveau_occ = 'SOUS-UTILISATION'

# Hopital 5
if h5_taux_occ > 95:
    h5_niveau_occ = 'CRITIQUE — saturation, transferts a organiser'
elif h5_taux_occ > 85:
    h5_niveau_occ = 'ELEVE — capacite limite, renforcement prevu'
elif h5_taux_occ > 70:
    h5_niveau_occ = 'OPTIMAL'
else:
    h5_niveau_occ = 'SOUS-UTILISATION'

# Comptage hopitaux en saturation
nb_hopitaux_saturation = 0

if h1_taux_occ > 95:
    nb_hopitaux_saturation = nb_hopitaux_saturation + 1
if h2_taux_occ > 95:
    nb_hopitaux_saturation = nb_hopitaux_saturation + 1
if h3_taux_occ > 95:
    nb_hopitaux_saturation = nb_hopitaux_saturation + 1
if h4_taux_occ > 95:
    nb_hopitaux_saturation = nb_hopitaux_saturation + 1
if h5_taux_occ > 95:
    nb_hopitaux_saturation = nb_hopitaux_saturation + 1

# ============================================================
# === SECTION H : CLASSIFICATION COUVERTURE VACCINALE (NEW S3)
# Normes OMS — seuils definis dans SECTION A (SEUIL_OMS_COUVERTURE_VACCIN = 95.0)
# ============================================================

# Donnees couverture vaccinale par departement
dep1_nom        = 'Brazzaville'
dep1_population = 450_000
dep1_vaccines   = 418_500
dep1_taux       = round(dep1_vaccines / dep1_population * 100, 1)  

dep2_nom        = 'Pointe-Noire'
dep2_population = 280_000
dep2_vaccines   = 229_600
dep2_taux       = round(dep2_vaccines / dep2_population * 100, 1)  

dep3_nom        = 'Pool'
dep3_population = 120_000
dep3_vaccines   = 54_000
dep3_taux       = round(dep3_vaccines / dep3_population * 100, 1)  

dep4_nom        = 'Sangha'
dep4_population = 85_000
dep4_vaccines   = 35_700
dep4_taux       = round(dep4_vaccines / dep4_population * 100, 1)  

# Classification — on utilise SEUIL_OMS_COUVERTURE_VACCIN (95.0) de la SECTION A

# Departement 1 — Brazzaville
if dep1_taux < 50:
    dep1_statut = 'ZONE CRITIQUE — campagne urgence immediate'
    dep1_couleur = '[ROUGE]'
elif dep1_taux < 80:
    dep1_statut = 'ZONE A RISQUE — campagne renforcee requise'
    dep1_couleur = '[ORANGE]'
elif dep1_taux < SEUIL_OMS_COUVERTURE_VACCIN:   
    dep1_statut = 'ZONE INSUFFISANTE — objectif OMS non atteint'
    dep1_couleur = '[JAUNE]'
else:
    dep1_statut = 'ZONE OMS CONFORME'
    dep1_couleur = '[VERT]'

# Departement 2 — Pointe-Noire
if dep2_taux < 50:
    dep2_statut = 'ZONE CRITIQUE — campagne urgence immediate'
    dep2_couleur = '[ROUGE]'
elif dep2_taux < 80:
    dep2_statut = 'ZONE A RISQUE — campagne renforcee requise'
    dep2_couleur = '[ORANGE]'
elif dep2_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dep2_statut = 'ZONE INSUFFISANTE — objectif OMS non atteint'
    dep2_couleur = '[JAUNE]'
else:
    dep2_statut = 'ZONE OMS CONFORME'
    dep2_couleur = '[VERT]'

# Departement 3 — Pool
if dep3_taux < 50:
    dep3_statut = 'ZONE CRITIQUE — campagne urgence immediate'
    dep3_couleur = '[ROUGE]'
elif dep3_taux < 80:
    dep3_statut = 'ZONE A RISQUE — campagne renforcee requise'
    dep3_couleur = '[ORANGE]'
elif dep3_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dep3_statut = 'ZONE INSUFFISANTE — objectif OMS non atteint'
    dep3_couleur = '[JAUNE]'
else:
    dep3_statut = 'ZONE OMS CONFORME'
    dep3_couleur = '[VERT]'

# Departement 4 — Sangha
if dep4_taux < 50:
    dep4_statut = 'ZONE CRITIQUE — campagne urgence immediate'
    dep4_couleur = '[ROUGE]'
elif dep4_taux < 80:
    dep4_statut = 'ZONE A RISQUE — campagne renforcee requise'
    dep4_couleur = '[ORANGE]'
elif dep4_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dep4_statut = 'ZONE INSUFFISANTE — objectif OMS non atteint'
    dep4_couleur = '[JAUNE]'
else:
    dep4_statut = 'ZONE OMS CONFORME'
    dep4_couleur = '[VERT]'

# Comptage zones vaccinales critiques
nb_zones_critiques = 0

if dep1_taux < 50:
    nb_zones_critiques = nb_zones_critiques + 1
if dep2_taux < 50:
    nb_zones_critiques = nb_zones_critiques + 1
if dep3_taux < 50:
    nb_zones_critiques = nb_zones_critiques + 1
if dep4_taux < 50:
    nb_zones_critiques = nb_zones_critiques + 1

# ============================================================
# === SECTION I : RAPPORT D'ETAT GLOBAL AVEC ALERTES (NEW S3)
# ============================================================

print()
print('=' * 65)
print('  RAPPORT D ETAT GLOBAL — SYSTEME DE SANTE CONGO')
print('  Date : 15 janvier 2026 | Module S3 enrichi')
print('=' * 65)

# --- Statut des stocks medicaments ---
print()
print('  STATUT DES STOCKS MEDICAMENTS')
print('-' * 65)
print(f'  {med1_couleur} {med1_nom:<35} : {med1_statut}')
print(f'  {med2_couleur} {med2_nom:<35} : {med2_statut}')
print(f'  {med3_couleur} {med3_nom:<35} : {med3_statut}')
print(f'  {med4_couleur} {med4_nom:<35} : {med4_statut}')
print(f'  {med5_couleur} {med5_nom:<35} : {med5_statut}')
print(f'  Ruptures critiques : {nb_ruptures_meds} | Alertes stock : {nb_alertes_meds}')

# --- Statut occupation hopitaux ---
print()
print('  OCCUPATION DES HOPITAUX')
print('-' * 65)
print(f'  {h1_nom:<35} : {h1_taux_occ}% — {h1_niveau_occ}')
print(f'  {h2_nom:<35} : {h2_taux_occ}% — {h2_niveau_occ}')
print(f'  {h3_nom:<35} : {h3_taux_occ}% — {h3_niveau_occ}')
print(f'  {h4_nom:<35} : {h4_taux_occ}% — {h4_niveau_occ}')
print(f'  {h5_nom:<35} : {h5_taux_occ}% — {h5_niveau_occ}')
print(f'  Hopitaux en saturation (> 95%) : {nb_hopitaux_saturation}')

# --- Couverture vaccinale ---
print()
print('  COUVERTURE VACCINALE PAR DEPARTEMENT')
print('-' * 65)
print(f'  {dep1_couleur} {dep1_nom:<15} : {dep1_taux}% — {dep1_statut}')
print(f'  {dep2_couleur} {dep2_nom:<15} : {dep2_taux}% — {dep2_statut}')
print(f'  {dep3_couleur} {dep3_nom:<15} : {dep3_taux}% — {dep3_statut}')
print(f'  {dep4_couleur} {dep4_nom:<15} : {dep4_taux}% — {dep4_statut}')
print(f'  Zones vaccinales critiques (< 50%) : {nb_zones_critiques}')

# --- Resume executif global ---
print()
print('=' * 65)
print('  RESUME EXECUTIF — DR. ELENGA Pascal, DSS')
print('=' * 65)
print(f'  Ruptures stock     : {nb_ruptures_meds} medicament(s) en rupture critique')
print(f'  Alertes stock      : {nb_alertes_meds} medicament(s) en alerte')
print(f'  Hopitaux satures   : {nb_hopitaux_saturation} etablissement(s) > 95% occupation')
print(f'  Zones vaccin. crit.: {nb_zones_critiques} departement(s) sous 50%')

# Recommandation finale selon le niveau general
if nb_ruptures_meds >= 2 or nb_zones_critiques >= 2:
    print()
    print('  !! ALERTE GENERALE : Situation sanitaire necessitant une')
    print('     intervention ministerielle immediate.')
elif nb_ruptures_meds >= 1 or nb_hopitaux_saturation >= 1:
    print()
    print('  ATTENTION : Des indicateurs sont hors normes.')
    print('     Declencher les protocoles d urgence concernant.')
else:
    print()
    print('  Situation globalement sous controle.')
    print('     Maintenir la surveillance standard.')

print('=' * 65)
print('  Module charge avec succes. Pret pour Semaine 4.')
print('=' * 65)
