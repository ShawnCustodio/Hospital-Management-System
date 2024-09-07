from person import Doctor, Patient
from hospital import Hospital
import json

if __name__ == "__main__":
    hospital = Hospital()

    # Load existing data
    try:
        hospital.load_data('patients.json', 'doctors.json')
    except json.JSONDecodeError as e:
        print(f"Error loading JSON data: {e}")
    except FileNotFoundError:
        print("JSON file not found. Starting with an empty hospital.")

    # Add new entries
    doctor = Doctor(3, "Dr. Brown", 60, "M", "Neurology")
    patient = Patient(4, "Alice Green", 40, "F", "Migraines")

    hospital.add_person(doctor)
    hospital.add_person(patient)

    doctor.assign_patient(patient)

    # Save updated data
    hospital.save_data('patients.json', 'doctors.json')

    # Print information
    for doc in hospital.doctors:
        print(doc.get_doctor_info())

    for pat in hospital.patients:
        print(pat.get_medical_info())
