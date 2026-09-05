from pydantic import BaseModel


class ConnectorBase(BaseModel):
    name: str
    type: str

class ConnectorCreateRequest(ConnectorBase):
    pass

class ConnectorResponse(ConnectorBase):
    id: str | None = None
    status: str