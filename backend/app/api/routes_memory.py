from fastapi import APIRouter
from ..memory.local_store import load_profile

router = APIRouter()

@router.get("/memory/profile/{user_id}")
def get_profile(user_id: str):
    return load_profile(user_id).model_dump()
