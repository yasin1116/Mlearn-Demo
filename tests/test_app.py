from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    data = response.json()
    assert "Removed" in data["message"]
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_delete_participant_rejects_missing_activity():
    response = client.delete("/activities/Does Not Exist/participants/test@example.com")

    assert response.status_code == 404
