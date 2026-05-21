from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    sections = Column(String)
    score = Column(String)


class QuestionResult(Base):
    __tablename__ = "question_results"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(Integer, ForeignKey("sessions.id"))

    question = Column(String)

    correct_answer = Column(String)

    user_answer = Column(String)

    is_correct = Column(Boolean)

    topic = Column(String)

    explanation = Column(String)