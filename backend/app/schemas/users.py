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

    class Config:
        from_attributes=True

class UserPayload(BaseModel):
    login: str
    name: str
    company: str
    location: str
    email: str
    picture: str
