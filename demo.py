from pydantic import BaseModel
class patient(BaseModel):
    name:str
    age:int
def patient_info(patient:patient):
    print(patient.name)
    print(patient.age)

patient_up = {'name':'Ahmad','age':23}
patient1 = patient(**patient_up)

patient_info(patient1)