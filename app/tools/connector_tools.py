from langchain_core.tools import BaseTool, tool
from app.services.connector_service import ConnectorService

def build_list_connectors_tool(service:ConnectorService) -> BaseTool :
    @tool
    def list_connectors() -> list[dict]:
        """List the enterprise connectors currently configured in AgentConnect."""
        connectors = service.get_connectors()

        return [
            {
                "id": connector.id,
                "name": connector.name,
                "type": connector.type,
                "status": connector.status,
            }
            for connector in connectors
        ]

    return list_connectors