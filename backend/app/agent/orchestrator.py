from typing import Dict, Any
from ..memory.local_store import load_profile, add_episode, update_preferences

def extract_preferences(text: str) -> Dict[str, str]:
    """
    Very small MVP heuristic.
    Later: replace with LLM extraction + validation.
    """
    t = text.lower()
    updates: Dict[str, str] = {}
    if "bilingual" in t or "en/es" in t or "english and spanish" in t:
        updates["language"] = "en+es"
    if "bullets" in t or "bullet" in t:
        updates["output_format"] = "bullets"
    if "table" in t:
        updates["output_format"] = "table"
    if "short" in t:
        updates["tone"] = "concise"
    if "professional" in t:
        updates["tone"] = "professional"
    if "executive brief" in t:
        updates["report_template"] = "executive_brief_v1"
    return updates

def run_agent(user_id: str, message: str) -> Dict[str, Any]:
    profile = load_profile(user_id)
    pref_updates = extract_preferences(message)
    if pref_updates:
        update_preferences(user_id, **pref_updates)
        profile = load_profile(user_id)

    # MVP response (no LLM yet). We’ll swap this for Foundry/AOAI next.
    prefs = profile.preferences
    response = {
        "answer": (
            f"Got it. I’ll respond using: output_format={prefs.output_format}, "
            f"tone={prefs.tone}, language={prefs.language}, template={prefs.report_template}.\n\n"
            "Next: I can generate an Executive Brief, Risk Summary, and Key Recommendations."
        ),
        "memory_used": {
            "preferences": profile.preferences.model_dump(),
            "recent_episodes_count": len(profile.recent_episodes),
        },
    }

    add_episode(
        user_id,
        content=f"User asked: {message}",
        metadata={"pref_updates": ",".join(pref_updates.keys()) if pref_updates else "none"},
    )

    return response
