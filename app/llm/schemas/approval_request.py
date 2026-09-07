from pydantic import BaseModel

class ApprovalRequest(BaseModel):
    approve: bool
    thread_id:str