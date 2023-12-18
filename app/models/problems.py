from typing import List
from typing import Optional
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

    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[Optional[str]]
    difficulty: Mapped[str] = mapped_column(String(6))
    approach: Mapped[Optional[str]]
    notes: Mapped[Optional[str]]
    problem_link: Mapped[Optional[str]]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    solutions: Mapped[List[DBSolution]] = relationship(lazy="selectin")
    tags: Mapped[List[DBTag]] = relationship(secondary=problem_tags, lazy="selectin")
