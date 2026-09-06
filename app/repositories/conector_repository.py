from app.models.connector import ConnectorEntity
from sqlalchemy.orm import Session

class ConnectorRepository:

    def __init__(self,db:Session):
        self.db = db

    def save(self, connector: ConnectorEntity):
        self.db.add(connector)
        self.db.commit()
        #self.db.refresh(connector)
        return connector

    def find_all(self) -> list[ConnectorEntity]:
       return (self.db.query(ConnectorEntity).all())