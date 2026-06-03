import uuid

from fastapi_users import schemas

class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    about: str


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    surname: str
    about: str


class UserUpdate(schemas.BaseUserUpdate):
    about: str
