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
