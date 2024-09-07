from flask import Flask, jsonify, request
from person import Doctor, Patient
from hospital import Hospital

app = Flask(__name__)
hospital = Hospital()

# Load existing data
try:
    hospital.load_data('patients.json', 'doctors.json')
except Exception as e:
    print(f"Error loading data: {e}")

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify([doctor.to_dict() for doctor in hospital.doctors])

@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify([patient.to_dict() for patient in hospital.patients])

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    data = request.json
    doctor = Doctor(**data)
    hospital.add_person(doctor)
    hospital.save_data('patients.json', 'doctors.json')
    return jsonify(doctor.to_dict()), 201

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.json
    patient = Patient(**data)
    hospital.add_person(patient)
    hospital.save_data('patients.json', 'doctors.json')
    return jsonify(patient.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
