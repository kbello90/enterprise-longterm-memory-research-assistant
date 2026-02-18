from fastapi import APIRouter
from pydantic import BaseModel
from ..agent.orchestrator import run_agent

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str = "demo-user"
    message: str

@router.post("/chat")
def chat(req: ChatRequest):
    return run_agent(req.user_id, req.message)
