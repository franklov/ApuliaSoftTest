from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
host: str = None
port: int = None

templates = Jinja2Templates(directory="./api/views")

@router.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse(
        "frontend.html", 
        {
            "request": request
        }
    )