import time

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = os.environ["MYSQLCONNECTION"]
for i in range(100):
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
    except:
        time.sleep(1)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()