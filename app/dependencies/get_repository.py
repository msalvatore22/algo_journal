from collections.abc import Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import repository, session
from app.models.base import Base


def get_repository(
    model: type[Base],
) -> Callable[[AsyncSession], repository.DBRepository]:
    def func(session: AsyncSession = Depends(session.get_db_session)):
        return repository.DBRepository(model, session)

    return func