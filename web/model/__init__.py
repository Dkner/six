from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

DeclarativeBase = declarative_base()
Engine = create_engine('mysql+pymysql://root:admin@localhost/test?charset=utf8')
DBSession = sessionmaker(bind=Engine)

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()