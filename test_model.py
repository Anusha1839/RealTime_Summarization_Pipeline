from faster_whisper import WhisperModel

print("Before model")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Model loaded successfully")