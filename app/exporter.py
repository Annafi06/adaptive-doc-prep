import json
import os


def export_session_results(session_id, results):

    os.makedirs("outputs", exist_ok=True)

    file_path = f"outputs/session_{session_id}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    return file_path