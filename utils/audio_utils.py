import ffmpeg
import os
def extract_audio(video_path):
  audio_path=os.path.splitext(video_path)[0]+".wav"
  (
    ffmpeg
    .input(video_path)
    .output(audio_path)
    .run(overwrite_output=True)
  
  )
  return audio_path