from fastapi import APIRouter
from app.services.connector_service import ConnectorService
from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)
from app.api.dependencies import get_connector_service
from fastapi import Depends


connector_router = APIRouter(
    prefix="/connectors"
);


@connector_router.get("",response_model=list[ConnectorResponse])
def get_connectors(service:ConnectorService = Depends(get_connector_service)) -> list :
   return service.get_connectors()

@connector_router.post("",response_model=ConnectorResponse)
def create_connector(request: ConnectorCreateRequest,service:ConnectorService = Depends(get_connector_service)):
   return service.create_connector(request)