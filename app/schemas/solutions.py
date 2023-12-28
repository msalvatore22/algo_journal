from pydantic import BaseModel
from datetime import time, datetime
from typing import List, Optional

class Solution(BaseModel):
    id: int
    code: Optional[str]
    duration: Optional[time]
    created: Optional[datetime]
    updated: Optional[datetime]
    problem_id: int
    user_id: int

class SolutionRequired(BaseModel):
    code: str
    duration: time
    problem_id: int
    user_id: int