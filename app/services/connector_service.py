from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)

class ConnectorService:

    SUPPORTED_TYPES = {
        "crm",
        "salesforce",
        "database"
    }

    
    def create_connector(self,request: ConnectorCreateRequest):

        if request.type not in self.SUPPORTED_TYPES:
            raise ValueError(f"unsupported connector type {request.type}")
        
        return ConnectorResponse(
            name = request.name,
            type = request.type
        )

    def get_connectors(self) -> list :
        return [
                ConnectorResponse(
                    name="salesforce",
                    type="crm",
                    status="ACTIVE"
                ),
                ConnectorResponse(
                    name="servicenow",
                    type="itsm",
                    status="ACTIVE"
                )
            ]