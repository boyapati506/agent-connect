from fastapi import FastAPI
from app.api.connectors import connector_router

app=FastAPI(
    title="Agent Connect",
    version="v1.0"
);

app.include_router(connector_router)

@app.get("/health")
def health() -> dict:
    return {
        "service" : "Agent Connect",
        "status" : "up"
    }
