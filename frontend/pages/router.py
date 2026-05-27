from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="frontend/templates")

@router.get("/index")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) # todo остановился тут
