
# CombinedModule.py

"""This module combines functionalities related to CRUD operations, SQLAlchemy models, and database sessions."""

## CRUD Enum Section

"""Defines an enumeration for CRUD (Create, Read, Update, Delete) operations."""

from enum import Enum

class CRUD(Enum):
    """Enumeration for CRUD operations."""
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    DELETE = 'delete'


## Models Section

"""Defines SQLAlchemy models for the database."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User model with fields id, username, and email."""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    posts = relationship("Post", back_populates="owner")
    
class Post(Base):
    """Post model with fields id, title, content, and owner_id."""
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    
    owner_id = Column(Integer, ForeignKey('users.id'))
    
    owner = relationship("User", back_populates="posts")


## Session Manager Section

"""Manages SQLAlchemy sessions and database engine."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./visuallama.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Database Agent Section

"""Defines a DatabaseAgent class for handling CRUD operations."""

class DatabaseAgent:
    """Class for handling database operations based on CRUD enum."""
    
    def __init__(self):
        """Initialize a new session."""
        self.session = SessionLocal()
        
    def db_handler(self, operation, model, **kwargs):
        """Handle CRUD operations for a given model."""
        try:
            if operation not in CRUD.__members__:
                raise ValueError(f"Invalid operation: {operation}. Must be one of {list(CRUD.__members__.keys())}.")
            operation_type = CRUD(operation).value

            if operation_type == CRUD.CREATE.value:
                new_entry = model(**kwargs)
                self.session.add(new_entry)
                self.session.commit()
                
            elif operation_type == CRUD.READ.value:
                query_result = self.session.query(model).filter_by(**kwargs).all()
                return query_result

            elif operation_type == CRUD.UPDATE.value:
                entries = self.session.query(model).filter_by(**kwargs.get('filter_by')).all()
                for entry in entries:
                    for key, value in kwargs.get('update_values').items():
                        setattr(entry, key, value)
                self.session.commit()

            elif operation_type == CRUD.DELETE.value:
                entries = self.session.query(model).filter_by(**kwargs).all()
                for entry in entries:
                    self.session.delete(entry)
                self.session.commit()

            return "Operation completed successfully."
        
        except Exception as e:
            return f"An error occurred: {e}"
