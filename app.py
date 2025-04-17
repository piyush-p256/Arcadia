# Directory Structure:
# esports_nexus_backend/
# ├── app.py                         # Main FastAPI app with all routes
# ├── models.py                      # Pydantic models for requests/responses
# ├── ai_modules/
# │   ├── __init__.py
# │   ├── realtime_coach.py        # Reinforcement learning-based coach
# │   ├── skill_gap_analyzer.py    # Clustering-based playstyle analyzer
# │   ├── highlight_generator.py   # CV-powered highlight generator
# │   └── knowledge_graph.py       # Neo4j integration
# └── utils/
#     ├── cv_utils.py               # CV helpers for detection
#     ├── nlp_utils.py              # NLP summarizer/commentary
#     └── audio_utils.py            # TTS and audio generation

# ---------------------- app.py ----------------------
from fastapi import FastAPI, UploadFile, File
from models import PlayerData, MatchData, HighlightRequest
from ai_modules import realtime_coach, skill_gap_analyzer, highlight_generator, knowledge_graph
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/analyze-skill")
def analyze_skill(data: PlayerData):
    return skill_gap_analyzer.analyze(data)

@app.post("/coach-feedback")
def coach_feedback(data: MatchData):
    return realtime_coach.generate_feedback(data)

@app.post("/generate-highlight")
def generate_highlight(request: HighlightRequest):
    return highlight_generator.create_personalized_highlight(request)

@app.get("/knowledge-graph/player/{player_id}")
def get_player_profile(player_id: str):
    return knowledge_graph.query_player_profile(player_id)

@app.post("/upload-match")
def upload_match(file: UploadFile = File(...)):
    # Placeholder for video ingestion
    return {"status": "uploaded", "filename": file.filename}

# ---------------------- models.py ----------------------
from pydantic import BaseModel
from typing import List, Optional

class PlayerData(BaseModel):
    player_id: str
    stats: dict
    recent_matches: List[dict]

class MatchData(BaseModel):
    match_id: str
    player_id: str
    events: List[dict]

class HighlightRequest(BaseModel):
    player_id: str
    match_id: str
    preferences: List[str]  # e.g. ["clutch", "multi-kill", "objective-steal"]
