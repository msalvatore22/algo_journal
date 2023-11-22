from pydantic import BaseModel
from datetime import datetime

class Tag(BaseModel):
    id: int
    name: str
    created: datetime
    updated: datetime
