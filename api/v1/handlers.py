from typing import Sequence

from pydantic import EmailStr
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.models import CreateUser
from db.models import User


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    """Select all users."""
    stmt = select(User)
    result = await session.execute(stmt)

    return result.scalars().all()


async def get_user_by_email(session: AsyncSession, email:EmailStr) -> User:
    """Select user by email."""
    stmt = select(User).where(User.email == email)
    result = await session.execute(stmt)

    return result.scalars().first()


async def post_new_user(session: AsyncSession, user:CreateUser) -> bool:
    """Create new user."""
    stmt = insert(User).values(user.model_dump())
    result = await session.execute(stmt)
    await session.commit()

    if result:
        return True

    return False


async def delete_user_by_email(session: AsyncSession, email:EmailStr) -> bool:
    """Delete user by email."""
    stmt = delete(User).where(User.email == email)
    result = await session.execute(stmt)
    await session.commit()

    if result:
        return True

    return False


async def update_user_by_email(session: AsyncSession,
                               email:EmailStr,
                               about:str) -> bool:
    """Update user by email."""
    stmt = update(User).where(User.email == email).values(about=about)
    result = await session.execute(stmt)
    await session.commit()

    if result:
        return True

    return False
