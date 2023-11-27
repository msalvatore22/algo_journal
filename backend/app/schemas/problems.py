from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
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
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    user_id: int

    class Config:
        from_attributes=True

class ProblemPayloadRequired(BaseModel):
    title: str
    description: str
    difficulty: str
    patterns: str
    notes: str
    leetcode_import: bool
    user_id: int

class ProblemPayload(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    patterns: Optional[str] = None
    notes: Optional[str] = None
    leetcode_import: Optional[bool] = None
    user_id: Optional[int] = None
