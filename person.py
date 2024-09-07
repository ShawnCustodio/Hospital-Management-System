class Person:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

class Patient(Person):
    def __init__(self, id, name, age, gender, medical_record, treatment_plan=None):
        super().__init__(id, name, age, gender)
        self.medical_record = medical_record
        self.treatment_plan = treatment_plan if treatment_plan is not None else []

    def add_treatment(self, treatment_plan):
        self.treatment_plan.append(treatment_plan)

    def get_medical_info(self):
        return f"{self.get_info()}, Medical Record: {self.medical_record}, Treatment Plan: {self.treatment_plan}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "medical_record": self.medical_record,
            "treatment_plan": self.treatment_plan
        })
        return data


class Doctor(Person):
    def __init__(self, id, name, age, gender, specialization, patients=None):
        super().__init__(id, name, age, gender)
        self.specialization = specialization
        self.patients = [Patient(**p) if isinstance(p, dict) else p for p in (patients or [])]

    def assign_patient(self, patient):
        self.patients.append(patient)

    def get_doctor_info(self):
        patient_names = ', '.join([p.name for p in self.patients])
        return f"{self.get_info()}, Specialization: {self.specialization}. Patients: {patient_names}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "specialization": self.specialization,
            "patients": [p.to_dict() for p in self.patients]  # Ensure all elements are Patient objects
        })
        return data
