from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os

class MovieDatabase:
    def __init__(self):
        self.DATABASE_URL = "postgresql://admin:admin123@localhost:5432/movies_db"
        self.engine = create_engine(self.DATABASE_URL, echo=True)

    def get_session(self) -> Generator[Session, None, None]:
        with Session(self.engine) as session:
            yield session

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)
db = MovieDatabase()

