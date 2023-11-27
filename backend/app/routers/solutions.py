from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated

from app.schemas.solutions import Solution, SolutionPayload, SolutionPayloadRequired
from app.database.repository import DBRepository
from app.models.solutions import DBSolution
from app.dependencies.get_repository import get_repository

SolutionRepository = Annotated[
    DBRepository[DBSolution],
    Depends(get_repository(DBSolution))
]

router = APIRouter()

@router.post("/solutions", status_code=status.HTTP_201_CREATED)
async def create_solution(
    data: SolutionPayload,
    repository: SolutionRepository
) -> Solution:
    solution = await repository.create(data.model_dump())
    return Solution.model_validate(solution)

@router.patch("/solutions/{id}", status_code=status.HTTP_200_OK)
async def patch_solution(
    data: SolutionPayload,
    id: int,
    repository: SolutionRepository
) -> Solution:
    solution = await repository.update(id, data.model_dump(exclude_unset=True))
    if solution is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solution does not exist"
        )
    return Solution.model_validate(solution)

@router.put("/solutions/{id}", status_code=status.HTTP_200_OK)
async def update_solution(
    data: SolutionPayloadRequired,
    id: int,
    repository: SolutionRepository
) -> Solution:
    solution = await repository.update(id, data.model_dump())
    if solution is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solution does not exist"
        )
    return Solution.model_validate(solution)

@router.get("/solutions/{id}", status_code=status.HTTP_200_OK)
async def get_solution(
    id: int,
    repository: SolutionRepository
) -> Solution:
    solution = await repository.get(id)
    if solution is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solution does not exist"
        )
    return Solution.model_validate(solution)

@router.get("/solutions", status_code=status.HTTP_200_OK)
async def get_solutions(
    repository: SolutionRepository
) -> list[Solution]:
    solutions = await repository.filter()
    if solutions is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solution does not exist"
        )
    return [Solution.model_validate(solution) for solution in solutions]

@router.delete("/solutions/{id}", status_code=status.HTTP_200_OK)
async def delete_solution(
    id: int,
    repository: SolutionRepository
) -> str:
    deletion = await repository.delete(id)
    if deletion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Solution does not exist"
        )
    return deletion