from app.repositories.conector_repository import ConnectorRepository
from app.repositories.in_memory_connector_repository import InMemoryConnectorRepository
from app.repositories.base_repository import BaseRepository
from app.services.connector_service import ConnectorService
from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from fastapi import Depends

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