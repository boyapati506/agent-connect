from app.schemas.connector import (ConnectorCreateRequest,ConnectorResponse,ConnectorBase)

class InMemoryConnectorRepository:

    def __init__(self):
        self._connector : list[ConnectorResponse] = []

    def save(self, connector: ConnectorCreateRequest):
        self._connector.append(connector)
        return connector

    def find_all(self):
        return self._connector