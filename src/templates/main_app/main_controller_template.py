main_controller_template: str = """from fastapi import APIRouter, Depends\n\n
from typing import Annotated\n\n
from app_services import AppService\n\n
AppService = Annotated[dict, Depends(AppService)]\n\n
router = APIRouter()\n\n
@router.get('/')\n
async def read_root(app_service: AppService):\n
    return app_service.get_message()\n
"""
