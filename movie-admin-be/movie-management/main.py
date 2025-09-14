from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from models.movie import MovieModel
from service import MovieService
from typing import List
from schema.movie_db import MovieDatabase
from sqlmodel import Session

app = FastAPI()
db = MovieDatabase()


@asynccontextmanager
async def on_startup():
    await db.create_db_and_tables()

@app.post('/movies', response_model=MovieModel)
async def create_movie(movie: MovieModel, session: Session = Depends(db.get_session)):
    service = MovieService(session)
    return await service.create_movie(movie)

@app.put('/movies/{movie_id}', response_model=MovieModel)
async def edit_movie(movie_id: int, movie: MovieModel, session: Session = Depends(db.get_session)):
    service = MovieService(session)
    result = await service.edit_movie(movie_id, movie)
    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")
    return result

@app.delete('/movies/{movie_id}')
async def delete_movie(movie_id: int, session: Session = Depends(db.get_session)):
    service = MovieService(session)
    success = await service.delete_movie(movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted"}

@app.get('/movies', response_model=List[MovieModel])
async def list_movies(session: Session = Depends(db.get_session)):
    service = MovieService(session)
    return await service.list_movies()
