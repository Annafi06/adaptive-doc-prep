import json
import os
from app.models import Session


def export_kb_snapshot(db, iteration_name):

    sessions = db.query(Session).order_by(
        Session.id.desc()
    ).limit(5).all()

    snapshot = []

    for s in sessions:

        snapshot.append({
            "session_id": s.id,
            "sections": s.sections,
            "score": s.score
        })

    folder = f"outputs/{iteration_name}"

    os.makedirs(folder, exist_ok=True)

    path = f"{folder}/kb_snapshot.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=4)

    return path