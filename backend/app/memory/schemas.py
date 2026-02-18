from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from datetime import datetime

class UserPreferences(BaseModel):
    output_format: str = "bullets"
    tone: str = "professional"
    language: str = "en"
    citation_style: str = "inline"
    report_template: str = "executive_brief_v1"

class MemoryItem(BaseModel):
    id: str
    type: str  # "preference" | "episode"
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, str] = Field(default_factory=dict)

class UserProfile(BaseModel):
    user_id: str
    preferences: UserPreferences = Field(default_factory=UserPreferences)
    recent_episodes: List[MemoryItem] = Field(default_factory=list)
