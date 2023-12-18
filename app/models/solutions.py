from typing import List
from typing import Optional
from datetime import time
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.models.sql_model import SQLModel
from app.models.base import Base

class DBSolution(Base, SQLModel):
    __tablename__ = "solutions"

    code: Mapped[Optional[str]]
    duration: Mapped[Optional[time]] = mapped_column(Time)
    solution_link: Mapped[Optional[str]]
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))