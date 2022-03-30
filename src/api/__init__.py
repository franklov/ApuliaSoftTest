from fastapi.websockets import WebSocket
import api.query
import api.frontend
from fastapi import APIRouter

hostAddress: str = ""
hostPort: str = ""
router = APIRouter()

router.include_router(api.frontend.router)
router.include_router(api.query.router)