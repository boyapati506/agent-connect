from fastapi import APIRouter
from app.llm.schemas.agent_request import AgentRequest
from app.llm.schemas.approval_request import ApprovalRequest
from app.services.llm_service import LLMService
from fastapi import Depends
from app.api.dependencies import get_llm_service

llm_router = APIRouter(prefix="/llm",tags=["llm"])

@llm_router.post(path="/ask")
def call_llm(request: AgentRequest,llm_service:LLMService = Depends(get_llm_service)):
    return {"response":llm_service.ask(request.message,request.thread_id)}

@llm_router.post(path="/approve")
def approve_llm(request: ApprovalRequest,llm_service:LLMService = Depends(get_llm_service)):
    return {"response":llm_service.approve(request.thread_id,request.approve)}