from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.schemas.users import User, UserPayload
from app.database.repository import DBRepository
from app.models.users import DBUser
from app.dependencies.get_repository import get_repository

UserRepository = Annotated[
    DBRepository[DBUser],
    Depends(get_repository(DBUser))
]

router = APIRouter()

@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserPayload,
    repository: UserRepository
) -> User:
    user = await repository.create(data.model_dump())
    return User.model_validate(user)

@router.get("/users/{id}", status_code=status.HTTP_200_OK)
async def get_user(
    id: int,
    repository: UserRepository
) -> User:
    user = await repository.get(id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    return User.model_validate(user)