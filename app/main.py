from fastapi import FastAPI
from app.schemas import QuizRequest
from app.llm_service import generate_mcqs
import json
from app.schemas import QuizRequest, SubmissionRequest
from app.database import SessionLocal
from app.models import Session, QuestionResult
from app.adaptive_engine import get_weak_topics
from app.analytics import calculate_topic_accuracy
from app.exporter import export_session_results
from app.logger import logger
from app.adaptive_engine import (
    get_weak_topics,
    get_previous_questions
)
from app.kb_snapshot import export_kb_snapshot

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Adaptive Document Preparation System Running"}


@app.post("/generate-quiz")
def generate_quiz(request: QuizRequest):

    db = SessionLocal()

    previous_questions = get_previous_questions(db)
    weak_topics = get_weak_topics(db)

    with open("data/sections.json", "r", encoding="utf-8") as f:
        sections_data = json.load(f)

    combined_text = ""

    for sec_id in request.sections:

        sec_id = str(sec_id)

        if sec_id in sections_data:
            combined_text += sections_data[sec_id]["content"]

    try:

        questions = generate_mcqs(
            combined_text,
            request.num_questions,
            weak_topics,
            previous_questions
        )

    except Exception as e:

        return {
            "error": str(e)
        }
    
    logger.info(f"Quiz generated for sections {request.sections}")

    return {
        "weak_topics_used": weak_topics,
        "questions": questions
    }

@app.post("/submit-answers")
def submit_answers(request: SubmissionRequest):

    db = SessionLocal()

    total_questions = len(request.answers)

    correct_count = 0

    session = Session(
        sections=str(request.sections),
        score=""
    )

    db.add(session)

    db.commit()

    db.refresh(session)

    results = []

    for ans in request.answers:

        is_correct = (
            ans.user_answer.strip().lower()
            ==
            ans.correct_answer.strip().lower()
        )

        if is_correct:
            correct_count += 1

        result = QuestionResult(
            session_id=session.id,
            question=ans.question,
            correct_answer=ans.correct_answer,
            user_answer=ans.user_answer,
            is_correct=is_correct,
            topic=ans.topic,
            explanation=ans.explanation
        )

        db.add(result)

        results.append({
            "question": ans.question,
            "is_correct": is_correct,
            "correct_answer": ans.correct_answer,
            "explanation": ans.explanation
        })

    score = f"{correct_count}/{total_questions}"

    session.score = score

    db.commit()

    export_path = export_session_results(
    session.id,
    results
    )

    logger.info(f"Session {session.id} submitted with score {score}")

    export_kb_snapshot(
        db,
        f"scenario_b_iter{session.id}"
    )

    return {
        "score": score,
        "results": results,
        "exported_file": export_path
    }

@app.get("/sessions")
def get_sessions():

    db = SessionLocal()

    sessions = db.query(Session).all()

    results = []

    for session in sessions:

        results.append({
            "session_id": session.id,
            "sections": session.sections,
            "score": session.score
        })

    return {
        "sessions": results
    }

@app.get("/session/{session_id}")
def get_session_details(session_id: int):

    db = SessionLocal()

    questions = db.query(QuestionResult).filter(
        QuestionResult.session_id == session_id
    ).all()

    results = []

    for q in questions:

        results.append({
            "question": q.question,
            "correct_answer": q.correct_answer,
            "user_answer": q.user_answer,
            "is_correct": q.is_correct,
            "topic": q.topic,
            "explanation": q.explanation
        })

    return {
        "session_id": session_id,
        "results": results
    }

@app.get("/analytics")
def analytics():

    db = SessionLocal()

    analytics_data = calculate_topic_accuracy(db)

    return {
        "analytics": analytics_data
    }