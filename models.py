from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database URL
DATABASE_URL = "sqlite:///users.db"

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

# Create a new SQLAlchemy session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base model for SQLAlchemy
Base = declarative_base()

# Define the Person model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


# Create the database schema
Base.metadata.create_all(engine)