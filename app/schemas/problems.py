from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.schemas.solutions import Solution
from app.schemas.tags import Tag

class Problem(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    approach: Optional[str] = None
    notes: Optional[str] = None
    user_id: Optional[int] = None
    problem_link: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    user_id: int

    class Config:
        from_attributes=True

class ProblemRequired(BaseModel):
    title: str
    description: str
    difficulty: str
    approach: str
    notes: str
    user_id: int

