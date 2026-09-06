from app.schemas.connector import (ConnectorCreateRequest,ConnectorResponse,ConnectorBase)
from typing import Protocol

class ConnectorRepository(Protocol):

    def save(self, connector: ConnectorCreateRequest):
        ...

    def find_all(self):
       ...