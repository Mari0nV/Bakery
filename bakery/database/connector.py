import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

DB_URI = os.environ.get("BK_DB_URI")
ENGINE = create_engine(DB_URI)
SESSION_MAKER = sessionmaker(bind=ENGINE)


def get_db_session() -> Generator[Session, None, None]:
    db_session = SESSION_MAKER()
    try:
        yield db_session
        db_session.commit()
    finally:
        db_session.close()
