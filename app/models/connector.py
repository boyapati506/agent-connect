from app.db.base import Base
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import String


class ConnectorEntity(Base):

    __tablename__ = "connectors"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )