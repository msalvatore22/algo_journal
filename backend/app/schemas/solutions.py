from pydantic import BaseModel
from datetime import time, datetime
from typing import List, Optional

class Solution(BaseModel):
    id: int
    code: str
    duration: time
    created: datetime
    updated: datetime
    problem_id: int
    user_id: int

class SolutionPayload(BaseModel):
    code: Optional[str] = None
    duration: Optional[time] = None
    problem_id: int
    user_id: int

class SolutionPayloadRequired(BaseModel):
    code: str
    duration: time
    problem_id: int
    user_id: int