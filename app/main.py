from fastapi import FastAPI
from app.schemas import QuizRequest
from app.llm_service import generate_mcqs
import json

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Adaptive Document Preparation System Running"}


@app.post("/generate-quiz")
def generate_quiz(request: QuizRequest):

    with open("data/sections.json", "r", encoding="utf-8") as f:
        sections_data = json.load(f)

    combined_text = ""

    for sec_id in request.sections:

        sec_id = str(sec_id)

        if sec_id in sections_data:
            combined_text += sections_data[sec_id]["content"]

    questions = generate_mcqs(
        combined_text,
        request.num_questions
    )

    return {
        "questions": questions
    }