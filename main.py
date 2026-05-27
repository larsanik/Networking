import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api.v1.users import router as users_router

from frontend.pages.router import router as frontend_router

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World! I'm here =o)"}

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])

app.include_router(frontend_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)