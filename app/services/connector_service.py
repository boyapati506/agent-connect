from app.schemas.connector import (ConnectorResponse,ConnectorCreateRequest)

class ConnectorService:

    
    def create_connector(request: ConnectorCreateRequest):
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