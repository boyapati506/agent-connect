from pydantic import BaseModel

class AgentDecision(BaseModel):
     action: str
     connector: str | None = None
     requires_approval: bool = False