from typing import List
from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.sql_model import SQLModel
from app.models.solutions import DBSolution
from app.models.tags import DBTag
from app.models.problem_tags import problem_tags
from app.models.base import Base

class DBProblem(Base, SQLModel):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str]
    difficulty: Mapped[str] = mapped_column(String(6))
    patterns: Mapped[Optional[str]]
    notes: Mapped[Optional[str]]
    leetcode_import: Mapped[bool]
    created: Mapped[datetime] = mapped_column(DateTime)
    updated: Mapped[datetime] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    solutions: Mapped[List[DBSolution]] = relationship()
    tags: Mapped[List[DBTag]] = relationship(
        secondary=problem_tags, back_populates="problems"
    )
