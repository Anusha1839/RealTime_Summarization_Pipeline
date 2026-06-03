print("Starting...")

from utils.transcriber import transcribe_audio

text = transcribe_audio("uploads/sample.wav")

with open(
    "outputs/transcript.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)

print("Transcript saved successfully!")

print("Transcription completed...")
print(text)