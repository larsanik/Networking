import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from starlette.requests import Request

from auth.db import User, get_user_db
from settings import secret

KEY =  secret.reset.get_secret_value()

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = KEY
    verification_token_secret = KEY

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        print(f"User {user.id} registered")

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        print(f"User {user.id} forgot password. Use token to reset: {token}")

    async def on_after_request_verify(
        self, user: User, token : str, request: Optional[Request] = None
    ) -> None:
        print(f"Verification request for {user.id}. Verification token: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)

