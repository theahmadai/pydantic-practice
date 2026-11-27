from pydantic import BaseModel,field_validator,EmailStr
from typing import Optional
class patient(BaseModel):
    name :str
    age:int
    email:EmailStr
    link:str
    @field_validator('email')
    @classmethod
    def field_(cls,value):
        valid_domain = ['hec.com','virtualuniversty.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("Note Allow")
        return value
    @field_validator('name',mode='before')
    @classmethod
    def upper_transformation(cls,value):
        return value.capitalize()

def patient_url(patient=patient):
    print(f"Name: {patient.name}")
    print(patient.age)
    print(patient.link)
patient_info = {'name':'ahmad','age':40,'link':'https://youtube.com','email':'the@hec.com'}
patient1=patient(**patient_info)
patient_url(patient1)