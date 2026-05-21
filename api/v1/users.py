from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.handlers import (get_all_users,
                             get_user_by_email,
                             post_new_user,
                             delete_user_by_email,
                             update_user_by_email
                             )
from api.v1.models import User, CreateUser
from db.connectors import get_db_session

# Берем в качестве идентификатора email. Считаем, что он будет уникальным.

router = APIRouter()


@router.get("/", response_model=List[User])
async def get_users(session: AsyncSession = Depends(get_db_session)):
    users = await get_all_users(session)

    if not users:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="Users not found")

    return users


@router.get("/{email}", response_model=User)
async def get_user(email: EmailStr,
                   session: AsyncSession = Depends(get_db_session)):
    user = await get_user_by_email(session, email=email)

    if not user:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="User not found")

    return user


@router.post("/", response_model=User)
async def add_user(user: CreateUser,
                   session: AsyncSession = Depends(get_db_session)):
    success = await post_new_user(session, user)

    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="User not created")

    return user


@router.delete("/{email}", response_model=EmailStr)
async def del_user(email: EmailStr,
                   session: AsyncSession = Depends(get_db_session)):
    success = await delete_user_by_email(session, email=email)

    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="User not deleted")

    return email


@router.patch("/{email}", response_model=str)
async def update_user(email: EmailStr,
                      about: str,
                      session: AsyncSession = Depends(get_db_session)):
    success = await update_user_by_email(session, email=email, about=about)

    if not success:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail="User not updated")

    return about
