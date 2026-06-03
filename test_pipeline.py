from utils.audio_utils import extract_audio
from utils.transcriber import transcribe_audio
from utils.cleaner import clean_text
from utils.chunking import chunk_text
from utils.gemini_utils import generate_summary

print("=" * 50)
print("REAL-TIME SUMMARIZATION PIPELINE")
print("=" * 50)

# Step 1: Extract Audio
print("\n[1] Extracting Audio...")

video_path = "uploads/sample.mp4"

audio_path = extract_audio(video_path)

print("Audio Saved:", audio_path)

# Step 2: Speech-to-Text
print("\n[2] Generating Transcript...")

transcript = transcribe_audio(audio_path)

with open(
    "outputs/transcript.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(transcript)

print("Transcript Saved")

# Step 3: Clean Transcript
print("\n[3] Cleaning Transcript...")

cleaned_text = clean_text(transcript)

with open(
    "outputs/cleaned_transcript.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(cleaned_text)

print("Cleaned Transcript Saved")

# Step 4: Chunking
print("\n[4] Chunking Transcript...")

chunks = chunk_text(
    cleaned_text,
    chunk_size=4000
)

print("Total Chunks:", len(chunks))

# Step 5: Gemini Summary
print("\n[5] Generating Final Summary...")

summary = generate_summary(cleaned_text)

with open(
    "outputs/final_summary.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(summary)

print("Summary Saved")

print("\n")
print("=" * 50)
print("FINAL SUMMARY")
print("=" * 50)

print(summary)