import psycopg2
import os
from sqlalchemy import create_engine
from functools import lru_cache

@lru_cache(maxsize=None)
def get_engine():
    return create_engine(os.getenv("DB_STRING"), pool_pre_ping=True)
