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
from . import DBSession, DeclarativeBase


class MovieModel(DeclarativeBase):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    brief = Column(String, default='')
    url = Column(String, default='')

    def __init__(self, movie):
        self.name = movie.get('name')
        self.brief = movie.get('brief')
        self.url = movie.get('url')

    @classmethod
    def insert(cls, movie_info):
        movie = MovieModel(movie_info)
        DBSession().add(movie)
        DBSession().flush()
        return movie

    @classmethod
    def get_all_movie(cls):
        return DBSession().query(cls).all()