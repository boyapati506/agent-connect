from app.repositories.conector_repository import ConnectorRepository
from app.repositories.in_memory_connector_repository import InMemoryConnectorRepository
from app.services.connector_service import ConnectorService

repository : ConnectorRepository = InMemoryConnectorRepository()

def get_connector_service() -> ConnectorService:

    return ConnectorService(repository)
