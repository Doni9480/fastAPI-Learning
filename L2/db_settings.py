from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine



class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite://data.sqlite3", echo=True)



def get_session():
    with Session(engine) as session:
        yield session
        session.commit()
