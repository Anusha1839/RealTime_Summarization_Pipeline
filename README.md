# 🎥 AI-Powered Video Summarization System

## 📌 Overview

AI-Powered Video Summarization System is an end-to-end Generative AI application that automatically converts long videos into concise, structured summaries.

The system extracts audio from uploaded videos, transcribes speech using Faster-Whisper, processes transcripts using Google Gemini AI, and generates meaningful summaries containing key insights and action items.

---

## 🚀 Features

- Upload video files through a web interface
- Automatic audio extraction from videos
- Speech-to-text transcription using Faster-Whisper
- AI-generated structured summaries
- Key points extraction
- Action items generation
- Responsive frontend interface
- FastAPI backend integration
- Secure API key management using environment variables

---

## 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- FastAPI
- Uvicorn

### AI & NLP

- Faster-Whisper
- Google Gemini API
- Prompt Engineering

### Audio Processing

- FFmpeg
- ffmpeg-python

### Data Validation

- Pydantic

### Environment Management

- Python Dotenv

---

## ⚙️ Workflow

1. Upload video through the frontend.
2. Extract audio using FFmpeg.
3. Transcribe speech using Faster-Whisper.
4. Clean and process transcript.
5. Generate structured summary using Gemini AI.
6. Display results on the frontend.

---

## 📊 Generated Output

The system generates:

### Title

- AI-generated title based on video content.

### Overview

- High-level summary of the video.

### Problem

- Main challenge discussed in the video.

### Solution

- Suggested solution or conclusion.

### Key Points

- Important concepts and insights extracted from the content.

### Action Items

- Practical actions identified from the discussion.

---

## 📚 Libraries Used

- fastapi
- uvicorn
- faster-whisper
- ffmpeg-python
- google-generativeai
- python-dotenv
- pydantic

---

## 🔗 API Endpoint

### Upload Video

```http
POST /upload
```

### Returns

- Title
- Overview
- Problem
- Solution
- Key Points
- Action Items

---

## 💻 Installation

### Clone Repository

```bash
git clone https://github.com/Anusha1839/RealTime_Summarization_Pipeline.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
uvicorn main:app --reload
```

---

## 🎯 Future Enhancements

- Real-Time Video Stream Summarization
- Searchable Summary History
- Database Integration
- Cloud Deployment
- PDF Export Support
- Multilingual Transcription
- Speaker Identification

---

## ⭐ Project Highlights

- End-to-end AI-powered video summarization pipeline
- Faster-Whisper based speech recognition
- Gemini-powered content understanding
- Structured summary generation
- Modern web interface using HTML, CSS, and JavaScript
- FastAPI backend architecture
- Secure API key handling with environment variables

---

## 👩‍💻 Author

**Dhanusha Ediga**

Aspiring AI Engineer | Machine Learning | NLP | Generative AI

GitHub: https://github.com/Anusha1839
