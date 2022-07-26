from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

from bakery.database.connector import ENGINE


Base = declarative_base()


class Hello(Base):
    __tablename__ = 'hello'
    name = Column(String, primary_key=True)


def configure_db():
    Base.metadata.create_all(ENGINE.engine)


if __name__ == '__main__':
    configure_db()
