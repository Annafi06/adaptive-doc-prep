from pydantic import BaseModel
from typing import List


class QuizRequest(BaseModel):
    sections: List[int]
    num_questions: int = 5