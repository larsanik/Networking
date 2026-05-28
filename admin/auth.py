from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form.get('username'), form.get('password')

        request.session.update({"token": "admin_session_active"})

        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        pass
        return True

authentication_backend = AdminAuth(secret_key="super-secret-admin-key")
