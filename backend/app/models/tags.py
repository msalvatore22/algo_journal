from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.models.sql_model import SQLModel
from app.models.base import Base

class DBTag(Base, SQLModel):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(String(30))
