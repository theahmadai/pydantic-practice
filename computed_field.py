from pydantic import BaseModel,computed_field
from typing import List
class patient(BaseModel):
    name : str
    age : int
    height :float
    weight : float
    allergies : list[str]
    @computed_field
    @property
    def compute_field(self) -> float:
        bmi = self.weight / self.height
        return bmi
def patient_infor(patient=patient):
    print('Name: ',patient.name)
    print('Age: ',patient.age)
    print('Height:',patient.height)
    print('Weight: ',patient.weight)
    print(f"Your calculated bmi is : {patient.compute_field}")
    print(patient.allergies)
patient_de={'name':'Ahmad','age':23,'allergies':{'asdama'},'height':5.1,'weight':45.5}
patient1 = patient(**patient_de)
patient_infor(patient1)