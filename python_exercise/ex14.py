class Patient:
    def __init__(self, patients_name, patients_id, age, gender, disease, status, contact_number):
        self.patients_name = patients_name
        self.patients_id = patients_id
        self.age = age
        self.gender = gender
        self.disease = disease
        self.status = status
        self.contact_number = contact_number

    def display_info(self):
        print(f"Patient Name: {self.patients_name}")
        print(f"Patient ID: {self.patients_id}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Status: {self.status}")
        print(f"Contact Number: {self.contact_number}")
        print("-" * 40)

# Example usage
if __name__ == "__main__":
    # Creating patient instances
    patient1 = Patient("John Doe", "P001", 30, "Male", "Flu", "Cured", "123-456-7890")
    patient2 = Patient("Jane Smith", "P002", 25, "Female", "Cold", "Not Cured", "098-765-4321")

    # Displaying patient information
    patient1.display_info()
    patient2.display_info()
