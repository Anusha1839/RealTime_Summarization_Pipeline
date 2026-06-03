from utils.chunking import chunk_text

with open(
    "outputs/transcript.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

chunks = chunk_text(text)

print("Number of Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk[:200])


    