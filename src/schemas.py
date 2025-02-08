from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date
from typing import Optional

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str  
    birth_date: date  
    additional_info: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
