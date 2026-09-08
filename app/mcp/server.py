from mcp.server import MCPServer
from app.services.connector_service import ConnectorService
from app.repositories.conector_repository import ConnectorRepository
from app.db.database import SessionLocal
from contextlib import contextmanager

mcp = MCPServer("AgentConnect")

@contextmanager
def get_connector_service():
    db= SessionLocal()
    try:
        repository = ConnectorRepository(db)
        service = ConnectorService(repository=repository)
        yield service
    finally:
        db.close()


@mcp.tool()
def get_connector_status(name: str) -> dict:
    """Get the status of an AgentConnect connector by name."""
    with get_connector_service() as service:
        return service.get_connector_by_name(name)
  

@mcp.tool()
def list_conectors() -> list:
    """List all configured AgentConnect connectors."""

    with get_connector_service() as service:
        connectors = service.get_connectors()
        return [connector.__dict__ for connector in connectors]
    
    # if not connector:
    #     return{
    #         "message":f"connector with name {name} not found"
    #     }
    # return{
    #     "name":connector["name"],
    #     "statue":connector["status"]
    # }
       
   

    # return {
    #     "name": name,
    #     "status": "ACTIVE"
    # }


if __name__ == "__main__":
    mcp.run()