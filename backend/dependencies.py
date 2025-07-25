from sqlmodel import Session, create_engine
from config import DatabaseConfig
from typing import Generator

# Create engine using configuration
engine = create_engine(DatabaseConfig.get_database_url(), echo=False)


def get_db_session() -> Generator[Session, None, None]:
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session


def get_database_engine():
    """Get the database engine"""
    return engine
