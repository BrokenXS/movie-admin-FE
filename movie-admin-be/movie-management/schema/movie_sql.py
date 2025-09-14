
from sqlmodel import Field, SQLModel

class Movie(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=255, nullable=False)
    description: str | None = Field(default=None, nullable=True)
    year: int | None = Field(default=None, nullable=True)
