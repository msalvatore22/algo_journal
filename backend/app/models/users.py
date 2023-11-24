from typing import List
from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
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
    solutions: Mapped[List[DBSolution]] = relationship()
    problems: Mapped[List[DBProblem]] = relationship()
