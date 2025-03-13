from management import HospitalManagementSystem

def main():
    system = HospitalManagementSystem()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Admit Patient")
        print("2. Add Bill")
        print("3. Discharge Patient")
        print("4. View Patient Details")
        print("5. Show All Patients")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            patient_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            disease = input("Enter disease: ")
            system.admit_patient(patient_id, name, age, disease)

        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            patient = system.get_patient(patient_id)
            if patient:
                amount = float(input("Enter bill amount: "))
                patient.add_bill(amount)
            else:
                print("Patient not found!")

        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            system.discharge_patient(patient_id)

        elif choice == '4':
            patient_id = input("Enter patient ID: ")
            patient = system.get_patient(patient_id)
            if patient:
                patient.view_details()
            else:
                print("Patient not found!")

        elif choice == '5':
            system.show_all_patients()

        elif choice == '6':
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
