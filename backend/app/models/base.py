from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func
from sqlalchemy import DateTime, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs




class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    # created: Mapped[datetime.datetime] = mapped_column(
    #     DateTime(timezone=True), server_default=func.now()
    # )
    # updated: Mapped[datetime.datetime] = mapped_column(
    #     DateTime(timezone=True), onupdate=func.now()
    # )

    # __mapper_args__ = {"eager_defaults": True}
