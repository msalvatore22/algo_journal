from typing import List
from typing import Optional
from datetime import datetime, time
from sqlalchemy import DateTime
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.sql_model import SQLModel
from app.models.base import Base

class DBSolution(Base, SQLModel):
    __tablename__ = "solutions"

    code: Mapped[str]
    duration: Mapped[Optional[time]] = mapped_column(Time)
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))