import json
import os


def export_questions(iteration_name, questions):

    folder = f"outputs/{iteration_name}"

    os.makedirs(folder, exist_ok=True)

    path = f"{folder}/questions.json"

    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=4)

    return path