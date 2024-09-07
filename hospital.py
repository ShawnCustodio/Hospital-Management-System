import json
from person import Doctor, Patient

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.staff = []

    def load_data(self, patient_file, doctor_file):
        # Load patient data
        try:
            with open(patient_file, 'r') as file:
                patient_data = json.load(file)
                self.patients = [Patient(**data) for data in patient_data]
                print(f"Loaded patients data from {patient_file}:")
                print(self.patients)  # Debugging output
        except FileNotFoundError:
            print(f"{patient_file} not found. Starting with an empty patient list.")
        except json.JSONDecodeError:
            print(f"Error decoding {patient_file}. Starting with an empty patient list.")

        # Load doctor data
        try:
            with open(doctor_file, 'r') as file:
                doctor_data = json.load(file)
                self.doctors = [Doctor(**data) for data in doctor_data]
                print(f"Loaded doctors data from {doctor_file}:")
                print(self.doctors)  # Debugging output
        except FileNotFoundError:
            print(f"{doctor_file} not found. Starting with an empty doctor list.")
        except json.JSONDecodeError:
            print(f"Error decoding {doctor_file}. Starting with an empty doctor list.")

    def save_data(self, patient_file, doctor_file):
        # Print data to be saved
        print("Saving patients data:")
        patient_data = [patient.to_dict() for patient in self.patients]
        print(patient_data)  # Debugging output

        # Save patient data
        with open(patient_file, 'w') as file:
            json.dump(patient_data, file, indent=4)

        print("Saving doctors data:")
        doctor_data = [doctor.to_dict() for doctor in self.doctors]
        print(doctor_data)  # Debugging output

        # Save doctor data
        with open(doctor_file, 'w') as file:
            json.dump(doctor_data, file, indent=4)

    def add_person(self, person):
        if isinstance(person, Patient):
            self.patients.append(person)
        elif isinstance(person, Doctor):
            self.doctors.append(person)
        else:
            raise ValueError("Invalid Person Type")
        
    def find_person(self, person_id):
        for person_list in [self.patients, self.doctors, self.staff]:
            for person in person_list:
                if person.id == person_id:
                    return person.get_info()
        return "Person not found."
