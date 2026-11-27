from pydantic import BaseModel,AnyUrl,EmailStr,Field
from typing import Optional,List,Annotated
class patient(BaseModel):
    name:str = Field(max_length=5,strict=True)
    
    Email: Annotated[EmailStr,Field(max_length=50,description='This is the email:',examples='abc@gmail.com')]
    age:int
    contact_Detail:Optional[List['str']]
def patient_info(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.Email)

patient_up = {'name':'Ahmad','age':23,'Email':'the@gmail.com','contact_Detail':{'ahmad'}}
patient1 = patient(**patient_up)

patient_info(patient1)