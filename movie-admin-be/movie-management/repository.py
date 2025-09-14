

import select
from typing import List, Optional

from sqlmodel import Session
from models.movie import MovieModel
from schema.movie_sql import Movie

class MovieRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    async def create_movie(self, movie: MovieModel) -> MovieModel:
        db_movie = Movie(title=movie.title, description=movie.description, year=movie.year)
        self.db.add(db_movie)
        self.db.commit()
        self.db.refresh(db_movie)
        return MovieModel(id=db_movie.id, title=db_movie.title, description=db_movie.description, year=db_movie.year)

    async def edit_movie(self, movie_id: int, movie: MovieModel) -> Optional[MovieModel]:
        db_movie = await self.db.get(Movie, movie_id)
        if not db_movie:
            return None
        db_movie.title = movie.title
        db_movie.description = movie.description
        db_movie.year = movie.year
        await self.db.commit()
        await self.db.refresh(db_movie)
        return MovieModel(id=db_movie.id, title=db_movie.title, description=db_movie.description, year=db_movie.year)

    async def delete_movie(self, movie_id: int) -> bool:
        db_movie = await self.db.get(Movie, movie_id)
        if not db_movie:
            return False
        await self.db.delete(db_movie)
        await self.db.commit()
        return True

    async def list_movies(self) -> List[MovieModel]:
        result = await self.db.exec(select(Movie))
        db_movies = result.all()
        return [MovieModel(id=m.id, title=m.title, description=m.description, year=m.year) for m in db_movies]
