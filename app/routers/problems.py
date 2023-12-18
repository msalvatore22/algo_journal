from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.schemas.problems import Problem, ProblemPayload, ProblemPayloadRequired
from app.database.repository import DBRepository
from app.models.problems import DBProblem
from app.dependencies.get_repository import get_repository

ProblemRepository = Annotated[
    DBRepository[DBProblem],
    Depends(get_repository(DBProblem))
]

router = APIRouter()

@router.post("/problems", status_code=status.HTTP_201_CREATED)
async def create_problem(
    data: ProblemPayload,
    repository: ProblemRepository
) -> Problem:
    problem = await repository.create(data.model_dump())
    return Problem.model_validate(problem)

@router.patch("/problems/{id}", status_code=status.HTTP_200_OK)
async def patch_problem(
    data: ProblemPayload,
    id: int,
    repository: ProblemRepository
) -> Problem:
    problem = await repository.update(id, data.model_dump(exclude_unset=True))
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem does not exist"
        )
    return Problem.model_validate(problem)

@router.put("/problems/{id}", status_code=status.HTTP_200_OK)
async def update_problem(
    data: ProblemPayloadRequired,
    id: int,
    repository: ProblemRepository
) -> Problem:
    problem = await repository.update(id, data.model_dump())
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem does not exist"
        )
    return Problem.model_validate(problem)

@router.get("/problems/{id}", status_code=status.HTTP_200_OK)
async def get_problem(
    id: int,
    repository: ProblemRepository
) -> Problem:
    problem = await repository.get(id)
    if problem is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem does not exist"
        )
    return Problem.model_validate(problem)

@router.get("/problems", status_code=status.HTTP_200_OK)
async def get_problems(
    repository: ProblemRepository
) -> list[Problem]:
    problems = await repository.filter()
    if problems is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem does not exist"
        )
    return [Problem.model_validate(problem) for problem in problems]

@router.delete("/problems/{id}", status_code=status.HTTP_200_OK)
async def delete_problem(
    id: int,
    repository: ProblemRepository
) -> str:
    deletion = await repository.delete(id)
    if deletion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Problem does not exist"
        )
    return deletion