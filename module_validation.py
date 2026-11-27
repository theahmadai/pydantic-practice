from pydantic import BaseModel,EmailStr,model_validator
from typing import Dict,Optional
class patient(BaseModel):
    name:str
    age:int

    contact_details:Optional[Dict[str,str]]
    @model_validator(mode='after')
    @classmethod
    def verify(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details :
            raise ValueError('Not, Amissionable')
        else:
            return model
def patient_m(patient=patient):
    print(patient.name)
    print(patient.age)


patient_info={'name':'Ahmad','age':65,'contact_details':{'phone':'3454532','emergency':'3543333'}}
patient1 = patient(**patient_info)
patient_m(patient1)