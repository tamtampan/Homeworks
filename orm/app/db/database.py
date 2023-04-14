from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

MYSQL_URL = f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@" \
            f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME}"


engine = create_engine(MYSQL_URL, echo=True)

# existing_databases = engine.execute("SHOW DATABASES;")
#
# existing_db = [d[0] for d in databases]

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db(): # generatorska funkcija
    db = SessionLocal()
    try:
        yield db # breake i return u isto vreme xD
    finally:
        db.close()
    return db
