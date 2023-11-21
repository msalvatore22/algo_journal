from typing import List
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.base import SQLModel
from app.models.solutions import DBSolution
from app.models.problems import DBProblem

class DBUser(SQLModel):
    ___tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    name: Mapped[str]
    company: Mapped[Optional[str]]
    location: Mapped[str]
    email: Mapped[str]
    picture: Mapped[Optional[str]]
    created: Mapped[DateTime]
    updated: Mapped[DateTime]
    solutions: Mapped[List[DBSolution]] = relationship()
    problems: Mapped[List[DBProblem]] = relationship()
