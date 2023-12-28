from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.schemas.solutions import Solution
from app.schemas.problems import Problem

class User(BaseModel):
    id: int
    login: Optional[str]
    name: Optional[str]
    company: Optional[str]
    location: Optional[str]
    email: Optional[str]
    picture: Optional[str]
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

    class Config:
        from_attributes=True

class UserRequired(BaseModel):
    login: str
    name: str
    company: str
    location: str
    email: str
    picture: str

