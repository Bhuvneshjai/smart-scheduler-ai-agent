from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Allow CORS for frontend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    return FileResponse("frontend/index.html")

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'google-credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
calendar_service = build('calendar', 'v3', credentials=credentials)

# Input schema from frontend
class UserMessage(BaseModel):
    message: str
    duration: Optional[int] = None
    preferred_day: Optional[str] = None
    time_of_day: Optional[str] = None

# Calendar availability checker
def get_available_slots(duration_minutes=60, day_preference="Tuesday", time_of_day="afternoon"):
    now = datetime.datetime.utcnow()
    start_of_day = now.replace(hour=12, minute=0, second=0)
    if time_of_day == "morning":
        start_of_day = now.replace(hour=8, minute=0, second=0)
    elif time_of_day == "evening":
        start_of_day = now.replace(hour=17, minute=0, second=0)
    end_of_day = start_of_day + datetime.timedelta(hours=4)

    events_result = calendar_service.freebusy().query(
        body={
            "timeMin": start_of_day.isoformat() + 'Z',
            "timeMax": end_of_day.isoformat() + 'Z',
            "timeZone": 'UTC',
            "items": [{"id": 'primary'}]
        }
    ).execute()

    busy_times = events_result['calendars']['primary']['busy']
    if not busy_times:
        return [start_of_day.isoformat()]
    return []

# Generate a response using Gemini
def chat_with_gpt(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error from Gemini: {str(e)}"

@app.get("/models")
async def list_models():
    try:
        return {"models": [m.name for m in genai.list_models()]}
    except Exception as e:
        return {"error": str(e)}

# Main chat API endpoint
@app.post("/chat")
async def chat(msg: UserMessage):
    prompt = (
        f"User wants to schedule a meeting. "
        f"Message: {msg.message}. "
        f"Duration: {msg.duration or 60} mins. "
        f"Day: {msg.preferred_day or 'Tuesday'}. "
        f"Time: {msg.time_of_day or 'afternoon'}. "
        f"Suggest a suitable time for a meeting."
    )
    reply = chat_with_gpt(prompt)
    available = get_available_slots(
        msg.duration or 60,
        msg.preferred_day or "Tuesday",
        msg.time_of_day or "afternoon"
    )
    return {"reply": reply, "available_slots": available}
