from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.conf.config import settings

# Create the database engine
engine = create_engine(settings.database_url)

# Create a session for database interaction
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for defining models
Base = declarative_base()

def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_database():
    """Function to check database connection"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1")).fetchone()
            if result:
                print("✅ Database connection is OK")
                return True
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        return False
