from utils.gemini_utils import generate_structured_summary

with open(
    "outputs/cleaned_transcript.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

result = generate_structured_summary(text)

import json

print(json.dumps(result, indent=4))