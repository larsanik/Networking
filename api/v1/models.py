from typing import Optional

from pydantic import BaseModel, EmailStr, UUID4


class User(BaseModel):
    id: Optional[UUID4] = None
    name: str
    surname: str
    email: Optional[EmailStr] = None
    about: Optional[str] = None


class CreateUser(BaseModel):
    name: str
    surname: str
    email: Optional[EmailStr] = None
    about: Optional[str] = None

