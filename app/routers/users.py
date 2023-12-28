from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy import select
from app.schemas.users import User, User, UserRequired
from app.schemas.problems import Problem
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
    data: User,
    repository: UserRepository
) -> User:
    user = await repository.create(data.model_dump())
    return User.model_validate(user)

@router.patch("/users/{id}", status_code=status.HTTP_200_OK)
async def patch_user(
    data: User,
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
    data: UserRequired,
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

@router.get("/users", status_code=status.HTTP_200_OK)
async def get_users(
    repository: UserRepository
) -> list[User]:
    users = await repository.filter()
    if users is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    return [User.model_validate(user) for user in users]

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

@router.get("/users/{id}/problems", status_code=status.HTTP_200_OK)
async def get_user_problems(
    id: int,
    repository: UserRepository
) -> list[Problem]:
    user = await repository.get(id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    user_problems = user.problems
    return [Problem.model_validate(user_problem) for user_problem in user_problems]