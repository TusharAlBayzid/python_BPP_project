class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.status = "Admitted"  # Default status
        self.bill = 0.0

    def discharge(self):
        self.status = "Discharged"

    def add_bill(self, amount):
        if amount > 0:
            self.bill += amount
            print(f"Added ${amount} to the bill of {self.name}.")
        else:
            print("Invalid bill amount!")

    def view_details(self):
        print(f"\nPatient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Disease: {self.disease}")
        print(f"Status: {self.status}")
        print(f"Bill: ${self.bill}")


