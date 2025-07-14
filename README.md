# 🧠 Smart Scheduler AI Agent

An intelligent voice/text-based chatbot assistant that schedules meetings using natural conversation.  
It integrates **Google Calendar**, **Gemini Pro (LLM)**, and **FastAPI**, with a simple interactive frontend.

---

## ✨ Features

- 🤖 Voice/Text chatbot (easily extendable)
- 📅 Google Calendar availability lookup
- 💬 LLM-powered (Gemini Pro by Google)
- ⚡ FastAPI backend with a browser interface
- 🧠 Context-aware prompts and natural replies
- ☁️ Ready for deployment on Render/Vercel

---

## 🛠 Tech Stack

| Layer         | Tool                    |
|---------------|-------------------------|
| LLM           | Google Gemini Pro       |
| Calendar API  | Google Calendar API     |
| Backend       | FastAPI                 |
| Frontend      | HTML + JavaScript       |
| Auth/Secrets  | `.env` with dotenv      |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Bhuvneshjai/smart-scheduler-ai-agent.git
cd smart-scheduler-ai-agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add Your API Keys

Create a `.env` file:

```env
GEMINI_API_KEY=your-google-ai-api-key
```

Also place your **Google service account JSON** as:
```
google-credentials.json
```

---

### 5. Run the App

```bash
uvicorn main:app --reload
```

Open in browser:  
👉 http://localhost:8000/

---

## 📁 Project Structure

```
smart_scheduler_ai_agent/
├── main.py
├── .env
├── requirements.txt
├── google-credentials.json
├── frontend/
│   └── index.html
└── README.md
```

---

## 📦 Generate Requirements from venv (if needed)

```bash
pip freeze > requirements.txt
```

---

## 📌 Notes

- You must enable **Google Calendar API** in your GCP Console
- This bot can be extended with:
  - Voice input (e.g., SpeechRecognition or WebRTC)
  - Google Meet auto-scheduling
  - Time zone logic

---

## 🧠 Credits

- [Google Gemini API](https://makersuite.google.com/app/apikey)
- [Google Calendar API Docs](https://developers.google.com/calendar/api)
- [FastAPI](https://fastapi.tiangolo.com)

---

## 🪄 License

2025 Smart Scheduler AI Team
