from fastapi import APIRouter
from app.services.connector_service import ConnectorService
from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)


connector_router = APIRouter(
    prefix="/connectors"
);

service = ConnectorService()

@connector_router.get("",response_model=list[ConnectorResponse])
def get_connectors() -> list :
   return service.get_connectors()

@connector_router.post("",response_model=ConnectorResponse)
def create_connector(request: ConnectorCreateRequest):
   return service.create_connector(request)