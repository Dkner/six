from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()
Engine = create_engine('mysql+pymysql://root:admin@localhost/test?charset=utf8')
DBSession = sessionmaker(bind=Engine)