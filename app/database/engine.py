import os
from sqlalchemy.ext.asyncio import create_async_engine
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()
db_string = os.getenv("DB_STRING")

@lru_cache(maxsize=None)
def get_async_engine():
    return create_async_engine(db_string, pool_pre_ping=True)
