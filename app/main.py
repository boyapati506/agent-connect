from fastapi import FastAPI
from app.api.connectors import connector_router
from app.db.base import Base
from app.db.database import engine

app=FastAPI(
    title="Agent Connect",
    version="v1.0"
);

app.include_router(connector_router)

Base.metadata.create_all(bind=engine)

