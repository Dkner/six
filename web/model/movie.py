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
from . import DBSession, DeclarativeBase, session_scope


class MovieModel(DeclarativeBase):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    brief = Column(String, default='')
    url = Column(String, default='')
    cover = Column(String, default='')

    def __init__(self, movie):
        self.name = movie.get('name')
        self.brief = movie.get('brief')
        self.url = movie.get('url')
        self.cover = movie.get('cover')

    @classmethod
    def insert(cls, movie_info):
        movie = MovieModel(movie_info)
        with session_scope() as session:
            session.add(movie)
            session.flush()
        return movie

    @classmethod
    def get_all_movie(cls):
        return DBSession().query(cls).all()