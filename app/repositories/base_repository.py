from app.models.connector import ConnectorEntity
from typing import Protocol

class BaseRepository(Protocol):

    def save(self, connector: ConnectorEntity):
        ...

    def find_all(self):
       ...