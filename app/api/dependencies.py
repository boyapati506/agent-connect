from app.repositories.conector_repository import ConnectorRepository
from app.repositories.in_memory_connector_repository import InMemoryConnectorRepository
from app.repositories.base_repository import BaseRepository
from app.services.connector_service import ConnectorService
from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from fastapi import Depends
from app.services.llm_service import LLMService
from app.llm.model_factory import get_model
from app.tools.registry import ToolRegistry
from app.tools.connector_tools import build_list_connectors_tool

def get_db() -> Generator[Session,None,None]:
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close() 

def get_connector_repository(
    db: Session = Depends(get_db),
) -> ConnectorRepository:
    return ConnectorRepository(db)        


def get_connector_service(repository: ConnectorRepository = Depends(get_connector_repository),) -> ConnectorService:
    return ConnectorService(repository)


def tool_registry( connector_service :ConnectorService = Depends(get_connector_service)) -> ToolRegistry:
    registry = ToolRegistry()
    list_connector_tools = build_list_connectors_tool(connector_service)
    registry.register(list_connector_tools)
    return registry

def get_llm_service(tool_registry:ToolRegistry = Depends(tool_registry)) -> LLMService:
    model = get_model()
    return LLMService(model,tool_registry)
