from app.schemas.connector import (ConnectorResponse)
from app.models.connector import ConnectorEntity

class InMemoryConnectorRepository:

    def __init__(self):
        self._connector : list[ConnectorResponse] = []

    def save(self, connector: ConnectorEntity):
        payload = ConnectorResponse(
            name=connector.name,
            type=connector.type,
            status="ACTIVE"
        )
        self._connector.append(payload)
        return connector

    def find_all(self):
        return self._connector