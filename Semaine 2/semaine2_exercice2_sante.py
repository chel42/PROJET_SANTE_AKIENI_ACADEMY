print()
print(f"\t==================================================================")
print(f"\t(AKIENI ACADEMY - Projet Sante Publique)")
print(f"\tSemaine 2 - Exercice 2: KPIs Sanitaires OMS")
print(f"\tVotre nom             : Michel De Marie BADJI")
print(f"\tDate                  : 21/06/2024")
print(f"\t==================================================================")
print()

# --- SECTION 1 : VARIABLES & DONNEES BRUTES ---
# TODO : Declararer toutes les variables ci-dessous
# 
budget_fcfa          = 87_450_000
nb_consultations_ext = 4823
nb_hospitalisations  = 1247
nb_deces             = 18
nb_lits_total        = 180
nb_lits_occupes      = 143
nb_medecins          = 22
nb_infirmiers        = 58
population_dept      = 128_000
taux_eur_fcfa        = 655.957
taux_usd_fcfa        = 600.0

# --- SECTION 2 : VARIABLES & DONNEES BRUTES ---
# TODO : Conversions devises
# 
budget_eur = budget_fcfa / taux_eur_fcfa
budget_usd = budget_fcfa / taux_usd_fcfa

# TODO : Indicateurs OMS
# 
densite_medicale = (nb_medecins / population_dept) * 1000
taux_mortalite_hospitaliere = (nb_deces / nb_hospitalisations) * 100
taux_occupation_lits = (nb_lits_occupes / nb_lits_total) * 100

# TODO : Division entiere & modulo
# 
budget_medicaments = int(budget_fcfa * 0.35)
cout_journalier_meds = 450_000
jours_rupture_stock = budget_medicaments // cout_journalier_meds
jours_restants = budget_medicaments % cout_journalier_meds 
parite_consultations = nb_consultations_ext % 2

if parite_consultations == 0:
    statut_parite = 'pair'
else:
    statut_parite = 'impair'

# TODO : Puissance pour projection
# 
budget_n_plus_2 = budget_fcfa * (1.08 ** 2)

# --- SECTION 3 : AFFICHAGE RAPPORT ---
# TODO : Afficher toutes les informations patient, consultation, hôpital et statut
#
print(f"\t === RAPPORT TRIMESTRIEL Q4 2025 - Hôpital Général Pointe-Noire === ")
print()
print(f"\t BUDGET")
print(f"\t   Depenses Q4        : {budget_fcfa:_} FCFA".replace('_', ' '))
print(f"\t   En euros           : {budget_eur:_.2f} EUR".replace('_', ' '))
print(f"\t   En dollars         : {budget_usd:_.2f} USD".replace('_', ' '))
print()
print(f"\t INDICATEURS OMS")
print(f"\t   Densité médicale   : {densite_medicale:.1f} / 1000 hab [Norme OMS : >= 2.3]")
print(f"\t   Taux mortalité     : {taux_mortalite_hospitaliere:.1f} %          [Seuil alerte : > 2%]")
print(f"\t   Taux occupation    : {taux_occupation_lits:.1f} %         [Optimale : 70-85%]")
print()
print(f"\t ANALYSE PHARMACIE")
print(f"\t   Budget médicaments : {budget_medicaments:_.0f} FCFA".replace('_', ' '))
print(f"\t   Jours de stock     : {jours_rupture_stock} jours")
print(f"\t   Jours depassement  : {0} jours")
print()
print(f"\t PROJECTION")
print(f"\t   Budget N+2 (8% / an) : {budget_n_plus_2:_.1f} FCFA".replace('_', ' '))
print()
if densite_medicale < 2.3:
    print(f"\t ALERTE : Densité médicale CRITIQUE ({densite_medicale:.1f} pour 1000 hab - norme OMS : 2.3)")
