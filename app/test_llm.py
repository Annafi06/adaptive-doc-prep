import json

with open("data/sections.json", "r", encoding="utf-8") as f:
    sections = json.load(f)

from llm_service import generate_mcqs

section_text = sections["1"]["content"]

questions = generate_mcqs(section_text)

print(json.dumps(questions, indent=4))