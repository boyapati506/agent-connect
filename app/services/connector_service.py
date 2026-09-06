from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)
from app.repositories.conector_repository import ConnectorRepository

class ConnectorService:

    def __init__(self,repository : ConnectorRepository):
        self.repository = repository

    SUPPORTED_TYPES = {
        "crm",
        "salesforce",
        "database"
    }

    
    def create_connector(self,request: ConnectorCreateRequest):

        if request.type not in self.SUPPORTED_TYPES:
            raise ValueError(f"unsupported connector type {request.type}")

        connector = ConnectorResponse(
            name=request.name,
            type=request.type,
            status="ACTIVE",
        )
        
        return self.repository.save(connector)

    def get_connectors(self) -> list[ConnectorResponse] :
        return self.repository.find_all()