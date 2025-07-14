# Smart Scheduler AI Agent

This is a voice-ready and web-based chatbot using FastAPI, GPT-4, and Google Calendar.

## How to Run

1. Place your Google Service Account JSON as `google-credentials.json`.
2. Add your OpenAI key to `.env` like:
   OPENAI_API_KEY=sk-...

3. Install packages:
   pip install -r requirements.txt

4. Run the app:
   uvicorn main:app --reload

5. Visit:
   http://localhost:8000
