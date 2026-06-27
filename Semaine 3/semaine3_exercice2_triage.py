# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if / elif / else, conditions composees or / and
# ============================================================

print('=' * 55)
print('  SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE')
print('  Protocole Manchester adapte — DSS Congo 2026')
print('=' * 55)
print()

# --- SAISIE DES DONNEES PATIENT ---
# input() avec conversion de types
nom_patient  = input('Nom du patient                           : ')
age_patient  = int(input('Age (annees)                             : '))
temperature  = float(input('Temperature (degres C, ex: 38.4)         : '))
spo2         = float(input('Saturation O2 en %  (ex: 96.0)           : '))
tension_syst = int(input('Tension systolique mmHg  (ex: 135)       : '))
douleur      = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VALIDATION DES PLAGES (S2 + S3 : conditions simples) ---
# Verifier que la temperature est dans une plage physiologiquement possible

erreur_saisie = False   # pour savoir si une erreur à ete detectée

if temperature < 35.0 or temperature > 43.0:
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')
    erreur_saisie = True

if spo2 < 50.0 or spo2 > 100.0:
    print('ERREUR : SpO2 hors plage — verifier le capteur')
    erreur_saisie = True

if tension_syst < 50 or tension_syst > 250:
    print('ERREUR : Tension hors plage — verifier le brassard')
    erreur_saisie = True

if douleur < 0 or douleur > 10:
    print('ERREUR : Douleur doit etre entre 0 et 10')
    erreur_saisie = True

if age_patient < 0 or age_patient > 120:
    print('ERREUR : Age invalide — verifier la saisie')
    erreur_saisie = True

# On continue seulement si toutes les saisies sont valides
if erreur_saisie == False:

    # --- TRIAGE (S3 nouveau : conditions composees avec or) ---
    # Niveau 1 : IMMEDIAT — au moins UNE condition critique (or)
    if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
        niveau_triage = '1 — IMMEDIAT'
        couleur_triage = '[ROUGE]'
        delai_pec      = '0 minute'
        action_triage  = 'Medecin present immediatement — code ROUGE active'

    # Niveau 2 :  URGENT — conditions moins critiques mais toujours urgentes
    elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
        niveau_triage = '2 — URGENT'
        couleur_triage = '[ORANGE]'
        delai_pec      = '< 10 minutes'
        action_triage  = 'Appel medecin senior'

    # Niveau 3 : URGENT DIFFERE
    elif temperature > 37.5 or douleur > 6:
        niveau_triage = '3 — URGENT DIFFERE'
        couleur_triage = '[JAUNE]'
        delai_pec      = '< 30 minutes'
        action_triage  = 'Infirmier — surveillance'

    # Niveau 4 : MOINS URGENT 
    else:
        niveau_triage = '4 — MOINS URGENT'
        couleur_triage = '[VERT]'
        delai_pec      = '< 120 minutes'
        action_triage  = 'File d attente standard'

    # --- DETERMINATION DU MOTIF PRINCIPAL ---
   
    if temperature > 39.5:
        motif_principal = f'Temperature {temperature} C > seuil 39.5 C'
    elif spo2 < 90:
        motif_principal = f'SpO2 {spo2}% < seuil 90%'
    elif tension_syst > 180:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 180 mmHg'
    elif temperature > 38.5:
        motif_principal = f'Temperature {temperature} C > seuil 38.5 C'
    elif spo2 < 94:
        motif_principal = f'SpO2 {spo2}% < seuil 94%'
    elif tension_syst > 140:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 140 mmHg'
    elif temperature > 37.5:
        motif_principal = f'Temperature {temperature} C > seuil 37.5 C'
    elif douleur > 6:
        motif_principal = f'Douleur {douleur}/10 > seuil 6'
    else:
        motif_principal = 'Tous les parametres dans les normes'

    # --- ETIQUETTES D'ETAT POUR CHAQUE PARAMETRE VITAL ---
    
    if temperature > 39.5:
        etat_temp = '[ANORMAL — > 39.5]'
    elif temperature > 38.5:
        etat_temp = '[ANORMAL — > 38.5]'
    elif temperature > 37.5:
        etat_temp = '[ANORMAL — > 37.5]'
    else:
        etat_temp = '[NORMAL]'

    if spo2 < 90:
        etat_spo2 = '[ANORMAL — < 90]'
    elif spo2 < 94:
        etat_spo2 = '[ANORMAL — < 94]'
    else:
        etat_spo2 = '[NORMAL]'

    if tension_syst > 180:
        etat_tension = '[ANORMAL — > 180]'
    elif tension_syst > 140:
        etat_tension = '[ANORMAL — > 140]'
    else:
        etat_tension = '[NORMAL]'

    if douleur > 6:
        etat_douleur = '[ANORMAL — > 6]'
    else:
        etat_douleur = '[NORMAL]'

    # --- AFFICHAGE FICHE TRIAGE ---
    print()
    print('=' * 55)
    print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
    print('=' * 55)
    print(f'  PARAMETRES VITAUX')
    print(f'  Temperature  : {temperature} C      {etat_temp}')
    print(f'  Saturation O2: {spo2} %        {etat_spo2}')
    print(f'  Tension syst.: {tension_syst} mmHg     {etat_tension}')
    print(f'  Douleur      : {douleur} / 10        {etat_douleur}')
    print('-' * 55)
    print(f'  NIVEAU DE TRIAGE : {niveau_triage}')
    print(f'  COULEUR          : {couleur_triage}')
    print(f'  PRISE EN CHARGE  : {delai_pec}')
    print(f'  ACTION           : {action_triage}')
    print('-' * 55)
    print(f'  Motif principal  : {motif_principal}')
    print('=' * 55)
