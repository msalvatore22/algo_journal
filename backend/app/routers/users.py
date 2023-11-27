from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.schemas.users import User, UserPayload, UserPayloadRequired
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

@router.patch("/users/{id}", status_code=status.HTTP_200_OK)
async def patch_user(
    data: UserPayload,
    id: int,
    repository: UserRepository
) -> User:
    user = await repository.update(id, data.model_dump(exclude_unset=True))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    return User.model_validate(user)

@router.put("/users/{id}", status_code=status.HTTP_200_OK)
async def update_user(
    data: UserPayloadRequired,
    id: int,
    repository: UserRepository
) -> User:
    user = await repository.update(id, data.model_dump())
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
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

@router.delete("/users/{id}", status_code=status.HTTP_200_OK)
async def delete_user(
    id: int,
    repository: UserRepository
) -> str:
    deletion = await repository.delete(id)
    if deletion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    return deletion