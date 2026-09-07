from fastapi import FastAPI
from app.api.connectors import connector_router
from app.db.base import Base
from app.db.database import engine
from app.api.llm_calls import llm_router

app=FastAPI(
    title="Agent Connect",
    version="v1.0"
);

app.include_router(connector_router)
app.include_router(llm_router)

Base.metadata.create_all(bind=engine)

