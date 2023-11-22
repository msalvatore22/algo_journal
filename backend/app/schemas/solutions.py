from pydantic import BaseModel
from datetime import time, datetime
from typing import List

class Solution(BaseModel):
    id: int
    code: str
    duration: time
    created: datetime
    updated: datetime
    problem_id: int
    user_id: int