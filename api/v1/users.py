from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr

from api.v1.models import User

# Берем в качестве идентификатора email. Считаем, что он будет уникальным.

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users():
    pass

@router.get("/{email}", response_model=User)
async def get_user():
    pass

@router.post("/", response_model=User)
async def add_user():
    pass

@router.delete("/{email}", response_model=EmailStr)
async def del_user():
    pass

@router.patch("/{email}", response_model=str)
async def update_user():
    pass
