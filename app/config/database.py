from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.config.settings import get_settings

_settings = get_settings()

engine = create_engine(
    _settings.database_url, echo=_settings.db_echo, pool_pre_ping=True
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db() -> Iterator[Session]:
    """Yield one session per request and always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()