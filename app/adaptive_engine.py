from collections import Counter
from sqlalchemy.orm import Session
from app.models import QuestionResult
from app.models import QuestionResult


def get_weak_topics(db: Session):

    wrong_answers = db.query(QuestionResult).filter(
        QuestionResult.is_correct == False
    ).all()

    topics = [q.topic for q in wrong_answers]

    topic_counts = Counter(topics)

    weak_topics = [
        topic
        for topic, count in topic_counts.items()
        if count >= 2
    ]

    return weak_topics

def get_previous_questions(db):

    previous = db.query(
        QuestionResult.question
    ).all()

    return [p[0] for p in previous]