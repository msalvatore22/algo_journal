from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from sqlalchemy import DateTime, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs




class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    updated = Column(DateTime(timezone=True), 
                       default=None, onupdate=datetime.datetime.utcnow)

