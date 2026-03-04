from fastapi import APIRouter
from app.services.attack_services import find_attack_path

router = APIRouter()

@router.get("/attack-path")
def attack_path(entry: str, target: str):
    return find_attack_path(entry, target)