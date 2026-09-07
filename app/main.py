from fastapi import FastAPI
from app.api.connectors import connector_router
from app.db.base import Base
from app.db.database import engine
from app.api.llm_calls import llm_router
from contextlib import asynccontextmanager
from fastapi import FastAPI
from langgraph.checkpoint.postgres import PostgresSaver

from app.db.database import LANGGRAPH_DATABASE_URL

@asynccontextmanager
async def lifespan(app: FastAPI):

    with PostgresSaver.from_conn_string(
        LANGGRAPH_DATABASE_URL
    ) as check_pointer:

        check_pointer.setup()

        app.state.check_pointer = check_pointer

        print("CHECKPOINTER INITIALIZED")

        yield

app=FastAPI(
    title="Agent Connect",
    version="v1.0",
    lifespan=lifespan
);

app.include_router(connector_router)
app.include_router(llm_router)

Base.metadata.create_all(bind=engine)

