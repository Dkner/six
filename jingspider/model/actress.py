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


class ActressModel(DeclarativeBase):
    __tablename__ = 'tb_actress'

    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    head_icon = Column(String, default='')
    birth = Column(String, default='')
    height = Column(Integer, default=0)
    weight = Column(Integer, default=0)
    cup = Column(String, default='')
    bust = Column(Integer, default=0)
    waist = Column(Integer, default=0)
    hip = Column(Integer, default=0)
    rate = Column(Integer, default=0)

    @classmethod
    def convert_dict_2_obj(cls, actress_dict):
        actress = ActressModel()
        for k, v in actress_dict.items():
            if hasattr(ActressModel, k) and v is not None:
                actress.__setattr__(k, v)
        return actress

    @classmethod
    def insert(cls, actress_dict):
        actress = cls.convert_dict_2_obj(actress_dict)
        with session_scope_context(DBSession) as session:
            session.add(actress)
        return actress

    @classmethod
    def get_all_actress(cls):
        return DBSession().query(cls).all()
