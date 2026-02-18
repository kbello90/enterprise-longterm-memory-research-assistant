import json
import os
from pathlib import Path
from typing import List
from datetime import datetime
from .schemas import UserProfile, MemoryItem, UserPreferences
from ..config import settings

def _user_path(user_id: str) -> Path:
    base = Path(settings.data_dir)
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{user_id}.json"

def load_profile(user_id: str) -> UserProfile:
    path = _user_path(user_id)
    if not path.exists():
        return UserProfile(user_id=user_id)

    data = json.loads(path.read_text(encoding="utf-8"))
    # pydantic handles parsing datetime strings if isoformat
    return UserProfile(**data)

def save_profile(profile: UserProfile) -> None:
    path = _user_path(profile.user_id)
    path.write_text(profile.model_dump_json(indent=2), encoding="utf-8")

def add_episode(user_id: str, content: str, metadata: dict | None = None) -> MemoryItem:
    profile = load_profile(user_id)
    item = MemoryItem(
        id=f"ep_{int(datetime.utcnow().timestamp())}",
        type="episode",
        content=content,
        metadata=metadata or {},
    )
    profile.recent_episodes = [item] + profile.recent_episodes[:9]  # keep last 10
    save_profile(profile)
    return item

def update_preferences(user_id: str, **kwargs) -> UserPreferences:
    profile = load_profile(user_id)
    prefs = profile.preferences.model_copy(update={k: v for k, v in kwargs.items() if v is not None})
    profile.preferences = prefs
    save_profile(profile)
    return prefs
