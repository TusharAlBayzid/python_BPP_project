from hospital import Patient

class HospitalManagementSystem:
    def __init__(self):
        self.patients = {}

    def admit_patient(self, patient_id, name, age, disease):
        if patient_id not in self.patients:
            patient = Patient(patient_id, name, age, disease)
            self.patients[patient_id] = patient
            print(f"Patient {name} admitted successfully with ID {patient_id}.")
        else:
            print("Patient ID already exists!")

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def discharge_patient(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient and patient.status == "Admitted":
            patient.discharge()
            print(f"Patient {patient.name} discharged successfully.")
        elif not patient:
            print("Patient not found!")
        else:
            print("Patient is already discharged.")

    def show_all_patients(self):
        if not self.patients:
            print("No patients in the hospital.")
        else:
            print("\n--- All Patients ---")
            for patient in self.patients.values():
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Status: {patient.status}, Bill: ${patient.bill}")
