from src.classes import *

patients = [
    PatientNormal("Ali", 30),
    PatientUrgent("Ahmed", 25),
    PatientVIP("Fatima", 40)
]
for patient in patients:
    traiter_patient(patient)
    print()
stats = statistiques(patients)
print("Statistiques :")
print(f"Nombre de patients : {stats['nombre_patients']}")
print(f"Patient prioritaire : {stats['patient_prioritaire']}")
print(f"Coût total des traitements : {stats['cout_total']} DH")
