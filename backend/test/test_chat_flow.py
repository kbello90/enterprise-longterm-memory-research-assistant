from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_chat_sets_preferences():
    r = client.post("/chat", json={"user_id": "u1", "message": "Use bullets and bilingual EN/ES executive brief"})
    assert r.status_code == 200
    data = r.json()
    prefs = data["memory_used"]["preferences"]
    assert prefs["output_format"] == "bullets"
    assert prefs["language"] == "en+es"
    assert prefs["report_template"] == "executive_brief_v1"

def test_profile_endpoint():
    r = client.get("/memory/profile/u1")
    assert r.status_code == 200
    prof = r.json()
    assert prof["user_id"] == "u1"
