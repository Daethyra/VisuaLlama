# sqlalchemy_database_operations.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

engine = create_engine('sqlite:///visuallama.db', echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Conversation(Base):
    __tablename__ = 'conversations'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    user_input = Column(Text)
    ai_response = Column(Text)
    timestamp = Column(DateTime)

class ObjectDetection(Base):
    __tablename__ = 'detections'
    
    id = Column(Integer, primary_key=True) 
    session_id = Column(Integer, ForeignKey('sessions.id'))
    image_path = Column(String)
    bbox_coords = Column(Text) # JSON encoded list
    confidence = Column(Float)
    timestamp = Column(DateTime)

class Session(Base):
    __tablename__ = 'sessions'
    
    id = Column(Integer, primary_key=True)
    conversations = relationship("Conversation", lazy='joined')
    detections = relationship("ObjectDetection", lazy='joined')

# Other model relationships    

class DatabaseAgent:

    def __init__(self):
        self.session = Session()
        
    # Methods for initialization, CRUD, migrations, etc   
        
    # Common preprocessed queries
    def get_session_conversations(self, session_id):
        return session.query(Conversation).filter(Conversation.session_id==session_id).order_by(Conversation.timestamp)
            
    def get_session_objects(self, session_id):
        return session.query(ObjectDetection).filter(ObjectDetection.session_id==session_id).order_by(ObjectDetection.timestamp)
            
# REST API, security, logging, events etc.