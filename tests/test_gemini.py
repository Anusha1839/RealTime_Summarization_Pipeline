from utils.gemini_utils import generate_summary

sample_text = """
Artificial Intelligence is transforming industries.
Machine learning enables systems to learn from data.
AI is widely used in healthcare, education and finance.
"""

summary = generate_summary(sample_text)

print(summary)