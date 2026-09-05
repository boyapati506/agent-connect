from fastapi import APIRouter

connector_router = APIRouter(
    prefix="/connectors"
);

@connector_router.get("")
def get_connectors() -> list :
    return [
        {
            "name": "salesforce",
            "type": "crm"
        },
        {
            "name": "servicenow",
            "type": "itsm"
        }
    ]