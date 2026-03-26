from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from datetime import datetime
from  app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    google_id = Column(String, unique=True, index=True)
    picture = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    
    raw_data = Column(JSON, nullable=True) 
    
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)