import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from admin.auth import authentication_backend
from api.v1.users import router as users_router

from frontend.pages.router import router as frontend_router

from admin.views import UserAdmin

from sqladmin import Admin
from db.connectors import engine

app = FastAPI()
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

app.include_router(frontend_router)

admin.add_view(UserAdmin)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)