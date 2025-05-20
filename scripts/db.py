# scripts/db.py 

from sqlalchemy import create_engine # for database connection
from dotenv import load_dotenv # for getting environment variables
import os # for using os dependent functions
from sqlalchemy.orm import sessionmaker # for creating a new session

load_dotenv() # load environment variables from .env

# get database connection settings from .env, with defaults for fallback
DB_USER = os.getenv("PG_USER", "postgres")
DB_PASSWORD = os.getenv("PG_PASSWORD", "1234")
DB_HOST = os.getenv("PG_HOST", "localhost")
DB_PORT = os.getenv("PG_PORT", "4000")
DB_NAME = os.getenv("PG_DATABASE", "spotify_db")

# build the database url in the SQLAlchemy format
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# resusable engine for connecting to the database
engine = create_engine(DATABASE_URL)

# session factory for ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)