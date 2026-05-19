from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    sections = Column(String)
    score = Column(String)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    correct_answer = Column(String)
    user_answer = Column(String)
    is_correct = Column(Boolean)
    topic = Column(String)