from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

class OperationLog(Base):
    __tablename__ = 'operation_logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    operation = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    detail = Column(Text)
