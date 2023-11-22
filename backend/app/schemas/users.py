from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.solutions import Solution
from app.schemas.problems import Problem

class User(BaseModel):
    id: int
    login: str
    name: str
    company: str
    location: str
    email: str
    picture: str
    created: datetime
    updated: datetime
    solutions: List[Solution]
    problems: List[Problem]
