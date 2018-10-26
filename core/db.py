import functools
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from contextlib import contextmanager

engine = create_engine('mysql+pymysql://root:admin@127.0.0.1:3306/test?charset=utf8',
                       pool_size=10, max_overflow=0)
DBSession = scoped_session(sessionmaker(bind=engine))
DeclarativeBase = declarative_base()


@contextmanager
def session_scope_context(session_factory):
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    # finally:
    #     session.close()