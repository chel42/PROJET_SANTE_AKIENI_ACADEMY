print()
print(f"\t==================================================================")
print(f"\t(AKIENI ACADEMY - Projet Sante Publique)")
print(f"\tSemaine 2 - Exercice 1: Fiche Patient CHU Brazzaville")
print(f"\tVotre nom             : Michel De Marie BADJI")
print(f"\tDate                  : 21/06/2024")
print(f"\t==================================================================")
print()

# --- SECTION 1 : VARIABLES PATIENT ---
# TODO : Declararer toutes les variables patient ci-dessous
# 
nom_patient = input("\tEntrez le nom du patient : ")
age_patient = input("\tEntrez l'âge du patient : ")
sexe_patient = input("\tEntrez le sexe du patient (M/F) : ")
departement_patient = input("\tEntrez le département du patient : ")
couverture_sociale = "CNSS"

# --- SECTION 2 : VARIABLES CONSULTATION ---
# TODO : Declarer les variables consultation
#
type_consultation = input("\tEntrez le type de consultation (Urgence/Consultation) : ")
diagnostic_principal = input("\tEntrez le diagnostic : ")
cout_consultation_fcfa = input("\tEntrez le coût de la consultation (FCFA) : ")
nb_consultations = input("\tEntrez le nombre de consultation : ")
remise_cnss_pct = 30.0


# --- SECTION 3 : VARIABLES HÔPITAL ---
# TODO : Declarer les variables hôpital
#
nom_hopital = "CHU Brazzaville"
ville_hopital = "Brazzaville"
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47

# --- SECTION 4 : CALCULS ---
# TODO : Calculer le cout total après remise CNSS
#
cout_total_fcfa = round(float(cout_consultation_fcfa) * (1 - remise_cnss_pct / 100), 2)

# TODO : Calculer le taux d'occupation (en pourcentage, arrondi à 1 decimale)
#
taux_occupation_pct = round((nb_lits_occupes / nb_lits_total) * 100, 1) 

# TODO : Calculer le ratio consultations par medecin (ce jour)
# HYpothèse : 120 consultations ont eu lieu ce mation dans tout l'hôpital
#
nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1) 

# Pause du programme pour permettre à l'utilisateur d'appuyer sur Entrée pour continuer la suite du programme
print()
input("\tAppuyer sur Entrée pour afficher la fiche patient...")

# --- SECTION 5 : CONTROLE DES DONNEES ---
# TODO : Vérifier si l'age est un entier via un try/except et afficher un message d'erreur si ce n'est pas le cas
#
try:
    age_patient = int(age_patient)  
except ValueError:
    print("Erreur : L'âge du patient doit être un entier.")
    exit(1)

# TODO : Vérifier si le sexe est soit 'M' soit 'F' et afficher un message d'erreur si ce n'est pas le cas
#
if sexe_patient not in ['M', 'F']:
    print("Erreur : Le sexe du patient doit être 'M' ou 'F'.")
    exit(1)

# TODO : Vérifier que le cout de la consultation est un nombre positif et afficher un message d'erreur si ce n'est pas le cas
#
try:
    cout_consultation_fcfa = float(cout_consultation_fcfa)
    if cout_consultation_fcfa < 0:
        print("Erreur : Le coût de la consultation doit être un nombre positif.")
        exit(1)
except ValueError:
    print("Erreur : Le coût de la consultation doit être un nombre.")
    exit(1)

# TODO : Vérifier si le nombre de consultations est un entier via un try/except et afficher un message d'erreur si ce n'est pas le cas
#
try:
    nb_consultations = int(nb_consultations)  
except ValueError:
    print("Erreur : Le nombre de consultation doit être un entier.")
    exit(1)


# --- SECTION 6 : AFFICHAGE DES INFORMATIONS ---
# TODO : Afficher toutes les informations patient, consultation, hôpital et statut
#
print()
print(f"\t==================================================================")
print(f"\t  FICHE PATIENT -- {nom_patient.upper()}")
print(f"\t==================================================================")
print(f"\t  Age                : {age_patient} ans")
print(f"\t  Sexe               : {sexe_patient.strip()}")
print(f"\t  Département        : {departement_patient.upper()}")
print(f"\t  Couverture sociale : {couverture_sociale}")
print(f"\t------------------------------------------------------------------")
print(f"\t  CONSULTATION")
print(f"\t  Type de consultation    : {type_consultation}")
print(f"\t  Diagnostic              : {diagnostic_principal}")
print(f"\t  Coût unitaire           : {cout_consultation_fcfa:} FCFA")
print(f"\t  Remise CNSS             : {remise_cnss_pct}%")
print(f"\t  COÛT TOTAL              : {cout_total_fcfa:,.0f} FCFA".replace(',', ' '))
print(f"\t------------------------------------------------------------------")
print(f"\t  HÔPITAL")
print(f"\t  Nom de l'hôpital        : {nom_hopital}")
print(f"\t  Ville                   : {ville_hopital}")
print(f"\t  Lits occupés            : {nb_lits_occupes} / {nb_lits_total} ({taux_occupation_pct}%)")
print(f"\t  Medecins actifs         : {nb_medecins_actifs}")
print(f"\t  Ratio consultations     : {ratio_consultations_medecin} consultations / medecin ce matin")
print(f"\t==================================================================")
print(f"\t  STATUT : prise en charge validée")
print(f"\t==================================================================")
print()
