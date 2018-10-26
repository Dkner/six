import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    SmallInteger,
    String,
    func,
    distinct,
    Boolean
)
from core.db import DBSession, DeclarativeBase, session_scope_context


class MovieModel(DeclarativeBase):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    brief = Column(String, default='')
    url = Column(String, default='')
    cover = Column(String, default='')

    @classmethod
    def convert_dict_2_obj(cls, movie_dict):
        movie = MovieModel()
        for k, v in movie_dict.items():
            if hasattr(MovieModel, k) and v is not None:
                movie.__setattr__(k, v)
        return movie

    @classmethod
    def insert(cls, movie_dict):
        movie = cls.convert_dict_2_obj(movie_dict)
        with session_scope_context(DBSession) as session:
            session.add(movie)
        return movie

    @classmethod
    def get_all_movie(cls):
        return DBSession().query(cls).all()


print(MovieModel.get_all_movie())
movie = MovieModel.insert({'name': 'movie2'})
print(movie.id)