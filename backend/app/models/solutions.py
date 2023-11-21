from typing import List
from typing import Optional
from sqlalchemy import DateTime
from sqlalchemy import Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.models.base import SQLModel

class DBSolution(SQLModel):
    ___tablename__ = "solutions"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str]
    duration: Mapped[Optional[Time]]
    created: Mapped[DateTime]
    updated: Mapped[DateTime]
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))