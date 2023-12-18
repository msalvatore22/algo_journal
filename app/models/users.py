from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from app.models.sql_model import SQLModel
from app.models.solutions import DBSolution
from app.models.problems import DBProblem
from app.models.base import Base

class DBUser(Base, SQLModel):
    __tablename__ = "users"

    login: Mapped[str]
    name: Mapped[str]
    company: Mapped[Optional[str]]
    location: Mapped[str]
    email: Mapped[str]
    picture: Mapped[Optional[str]]
    solutions: Mapped[List[DBSolution]] = relationship(lazy="selectin")
    problems: Mapped[List[DBProblem]] = relationship(lazy="selectin")
