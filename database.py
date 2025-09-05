from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import create_engine
engine = create_engine("sqlite:///mt.db")

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
      
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()