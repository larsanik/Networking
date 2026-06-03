import uuid

import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from admin.auth import authentication_backend
from api.v1.users import router as users_router
from auth.core import auth_backend
from auth.db import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead
from frontend.pages.router import router as frontend_router

from admin.views import UserAdmin

from sqladmin import Admin
from db.connectors import engine

app = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend]
)

app.add_middleware(SessionMiddleware, secret_key="super-secret-admin-key")

admin = Admin(app, engine=engine, authentication_backend=authentication_backend)

@app.get("/")
async def root():
        return RedirectResponse(url="/pages/index")

# @app.get("/")
# async def root():
#         return RedirectResponse(url="/admin/")


app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])

admin.add_view(UserAdmin)

app.include_router(frontend_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)