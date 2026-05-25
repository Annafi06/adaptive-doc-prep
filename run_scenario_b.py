import requests
import json
import os

BASE_URL = "http://127.0.0.1:8000"

iterations = [
    {
        "name": "scenario_b_iter1",
        "sections": [5, 8]
    },
    {
        "name": "scenario_b_iter2",
        "sections": [6, 8, 9]
    },
    {
        "name": "scenario_b_iter3",
        "sections": [8]
    }
]


for iteration in iterations:

    print(f"\nRunning {iteration['name']}")

    response = requests.post(
        f"{BASE_URL}/generate-quiz",
        json={
            "sections": iteration["sections"],
            "num_questions": 5
        }
    )

    quiz_data = response.json()

    os.makedirs(
        f"outputs/{iteration['name']}",
        exist_ok=True
    )

    with open(
        f"outputs/{iteration['name']}/questions.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(quiz_data, f, indent=4)

    fake_answers = []

    for q in quiz_data["questions"]:

        fake_answers.append({
            "question": q["question"],
            "correct_answer": q["correct_answer"],
            "user_answer": "Wrong Answer",
            "topic": q["topic"],
            "explanation": q["explanation"]
        })

    submit_response = requests.post(
        f"{BASE_URL}/submit-answers",
        json={
            "sections": iteration["sections"],
            "answers": fake_answers
        }
    )

    submission_data = submit_response.json()

    with open(
        f"outputs/{iteration['name']}/submission.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(submission_data, f, indent=4)

    print(f"Completed {iteration['name']}")