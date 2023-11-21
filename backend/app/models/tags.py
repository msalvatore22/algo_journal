from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.models.base import SQLModel

class DBTag(SQLModel):
    ___tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    created: Mapped[DateTime]
    updated: Mapped[DateTime]
