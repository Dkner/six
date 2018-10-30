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
    __tablename__ = 'tb_movie'

    id = Column(Integer, primary_key=True)
    title = Column(String, default='')
    code = Column(String, default='')
    cover = Column(String, default='')
    snapshot = Column(String, default='')
    rate = Column(Integer, default=0)
    path = Column(String, default='')

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
