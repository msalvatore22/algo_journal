import psycopg2
import os
from sqlalchemy.ext.asyncio import create_async_engine
from functools import lru_cache

@lru_cache(maxsize=None)
def get_async_engine():
    return create_async_engine(os.getenv("DB_STRING"), pool_pre_ping=True)
