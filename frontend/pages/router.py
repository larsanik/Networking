from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from api.v1.users import get_user

router = APIRouter(
    prefix="/pages",
    tags=["pages"]
)

templates = Jinja2Templates(directory="frontend/templates")

@router.get("/index")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html" )


@router.get("/card/{email}")
async def get_card(request: Request, user=Depends(get_user)):
    return templates.TemplateResponse(request, "card.html", {"user": user})
