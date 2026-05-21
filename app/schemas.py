from pydantic import BaseModel
from typing import List


class QuizRequest(BaseModel):
    sections: List[int]
    num_questions: int = 5

class AnswerItem(BaseModel):
    question: str
    correct_answer: str
    user_answer: str
    topic: str
    explanation: str


class SubmissionRequest(BaseModel):
    sections: List[int]
    answers: List[AnswerItem]