from models.movie import MovieModel
from repository import MovieRepository
from typing import List, Optional
from sqlmodel import Session
class MovieService:
    def __init__(self, db_session: Session):
        self.repo = MovieRepository(db_session)

    async def create_movie(self, movie: MovieModel) -> MovieModel:
        return await self.repo.create_movie(movie)

    async def edit_movie(self, movie_id: int, movie: MovieModel) -> Optional[MovieModel]:
        return await self.repo.edit_movie(movie_id, movie)

    async def delete_movie(self, movie_id: int) -> bool:
        return await self.repo.delete_movie(movie_id)

    async def list_movies(self) -> List[MovieModel]:
        return await self.repo.list_movies()