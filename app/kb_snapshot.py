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

    iteration_number = iteration_name.split("iter")[-1]

    path = f"{folder}/kb_snapshot_iter{iteration_number}.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=4)

    return path