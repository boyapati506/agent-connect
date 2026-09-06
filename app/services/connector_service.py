from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)
from app.repositories.base_repository import BaseRepository
from app.models.connector import ConnectorEntity


class ConnectorService:

    def __init__(self,repository : BaseRepository):
        self.repository = repository

    SUPPORTED_TYPES = {
        "crm",
        "salesforce",
        "database"
    }

    
    def create_connector(self,request: ConnectorCreateRequest):

        if request.type not in self.SUPPORTED_TYPES:
            raise ValueError(f"unsupported connector type {request.type}")

        connector = ConnectorEntity(
            name=request.name,
            type=request.type,
            status="ACTIVE",
        )
        
        saved=self.repository.save(connector)
        return ConnectorResponse(
            id= saved.id,
            name=saved.name,
            type=saved.type,
            status=saved.status
        )

    def get_connectors(self) -> list[ConnectorResponse] :

        connectors=self.repository.find_all()
        result:list[ConnectorResponse]=[]
        for connector in connectors:
            result.append(ConnectorResponse(
            id= connector.id,
            name=connector.name,
            type=connector.type,
            status=connector.status
        )
        )
        return result