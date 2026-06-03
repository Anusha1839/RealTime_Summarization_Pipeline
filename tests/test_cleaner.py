from utils.cleaner import clean_text

with open(
    "outputs/transcript.txt",
    "r",
    encoding="utf-8"
) as f:
    transcript = f.read()

cleaned_text = clean_text(transcript)

print(cleaned_text[:1000])