def test_get_projects(client):
    response = client.get("/api/projects")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_project_not_found(client):
    response = client.get("/api/projects/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_create_project(client):
    data = {
        "projectId": 12345,
        "title": "Test",
        "description": "Test",
        "deadline": "2026-01-01",
        "statusId": 1
    }

    response = client.post("/api/projects", json=data)

    assert response.status_code == 201
    assert response.json()["message"] == "Project created"