from sqlalchemy.orm import Session
from app.models import QuestionResult


def calculate_topic_accuracy(db: Session):

    results = db.query(QuestionResult).all()

    topic_stats = {}

    for result in results:

        topic = result.topic

        if topic not in topic_stats:
            topic_stats[topic] = {
                "total": 0,
                "correct": 0
            }

        topic_stats[topic]["total"] += 1

        if result.is_correct:
            topic_stats[topic]["correct"] += 1

    analytics = []

    for topic, stats in topic_stats.items():

        accuracy = (
            stats["correct"] / stats["total"]
        ) * 100

        analytics.append({
            "topic": topic,
            "accuracy": round(accuracy, 2),
            "attempts": stats["total"]
        })

    return analytics