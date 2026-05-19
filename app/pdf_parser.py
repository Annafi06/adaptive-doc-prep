import fitz
import re
import json

PDF_PATH = "data/SLATEFALL_DOSSIER.pdf"

doc = fitz.open(PDF_PATH)

full_text = ""

for page in doc:
    full_text += page.get_text()

pattern = r"(Section\s\d+\..*?)(?=Section\s\d+\.|\Z)"

matches = re.findall(pattern, full_text, re.DOTALL)

sections = {}

for idx, match in enumerate(matches, start=1):
    sections[idx] = {
        "content": match.strip()
    }

with open("data/sections.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=4)

print("Sections extracted successfully!")