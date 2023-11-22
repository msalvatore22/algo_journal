from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.solutions import Solution
from app.schemas.tags import Tag

class Problem(BaseModel):
    id: int
    title: str
    description: str
    difficulty: str
    patterns: str
    notes: str
    leetcode_import: bool
    created: datetime
    updated: datetime
    user_id: int
    solutions: List[Solution]
    tags: List[Tag]
