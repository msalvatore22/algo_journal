import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import StaticPool, exc
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator, Callable
from typing import Annotated

from app import main
from app.database.repository import DBRepository
from app.models.base import Base


@pytest.mark.anyio
async def test_read_root():
    async with AsyncClient(app=main.app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == { "message": "Server is running" }
