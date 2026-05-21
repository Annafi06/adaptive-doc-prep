from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_mcqs(
    section_text,
    num_questions=5,
    weak_topics=None
):
    weak_topics_text = ""

    if weak_topics:
        weak_topics_text = f"""
        Focus more on these weak topics:
        {', '.join(weak_topics)}
        """

    prompt = f"""
    Generate {num_questions} MCQs from the following text.

    Requirements:
    - Each MCQ must include:
      - question
      - 4 options
      - correct_answer
      - explanation
      - topic

    Return ONLY valid JSON.

    Example:

    [
      {{
        "question": "What is ...?",
        "options": [
          "A",
          "B",
          "C",
          "D"
        ],
        "correct_answer": "A",
        "explanation": "Because...",
        "topic": "Topic Name"
      }}
    ]

    {weak_topics_text}
    
    TEXT:
    {section_text}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    text = completion.choices[0].message.content.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "")

    try:
        return json.loads(text)

    except Exception as e:
        return {
            "error": str(e),
            "raw_response": text
        }