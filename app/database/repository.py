from typing import Generic, TypeVar

from sqlalchemy import BinaryExpression, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import Base

Model = TypeVar("Model", bound=Base)

class DBRepository(Generic[Model]):
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session
    
    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
    
    async def get(self, id: int) -> Model | None:
        return await self.session.get(self.model, id)
    
    async def update(self, id: int, data: dict) -> Model | None:
        instance = await self.session.get(self.model, id)
        if instance is None:
            return None
        for key, value in data.items():
            setattr(instance, key, value)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
    
    async def delete(self, id: int) -> str | None:
        instance = await self.session.get(self.model, id)
        if instance is None:
            return None
        await self.session.delete(instance)
        await self.session.commit()
        return f'User: {id} deleted'
    
    async def filter(
        self,
        *expressions: BinaryExpression,
    ) -> list[Model]:
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        return list(await self.session.scalars(query))