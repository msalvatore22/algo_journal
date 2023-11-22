from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from app.models.base import Base

problem_tags = Table(
    "problem_tags",
    Base.metadata,
    Column("problem_id", ForeignKey("problems.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)
