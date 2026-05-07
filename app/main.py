from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.db import engine

app = FastAPI(title="Project Service")

SCHEMA = "Volha_Platnitskaya_project"
TABLE = f"{SCHEMA}.Project"
STATUS_TABLE = f"{SCHEMA}.ProjectStatus"

@app.get("/api/projects")
def get_projects():

    query = text(f"SELECT * FROM {TABLE}")

    with engine.connect() as conn:
        result = conn.execute(query)
        return [dict(row._mapping) for row in result]


@app.get("/api/projects/{id}")
def get_project(id: int):

    query = text(f"""
        SELECT * FROM {TABLE}
        WHERE projectId = :id
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"id": id}).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Not found")

    return dict(result._mapping)

@app.post("/api/projects", status_code=201)
def create_project(project: dict):
    """
    {
        "projectId": 1,
        "title": "AI Project",
        "description": "Build model",
        "deadline": "2026-01-01",
        "statusId": 1
    }
    """

    query = text(f"""
        INSERT INTO {TABLE}
        (projectId, title, description, deadline, statusId)
        VALUES
        (:projectId, :title, :description, :deadline, :statusId)
    """)

    with engine.connect() as conn:
        conn.execute(query, project)
        conn.commit()

    return {"message": "Project created"}

@app.patch("/api/projects/{id}")
def update_project(id: int, body: dict):

    fields = []
    params = {"id": id}

    if "title" in body:
        fields.append("title = :title")
        params["title"] = body["title"]

    if "description" in body:
        fields.append("description = :description")
        params["description"] = body["description"]

    if "statusId" in body:
        fields.append("statusId = :statusId")
        params["statusId"] = body["statusId"]

    query = text(f"""
        UPDATE {TABLE}
        SET {", ".join(fields)}
        WHERE projectId = :id
    """)

    with engine.connect() as conn:
        conn.execute(query, params)
        conn.commit()

    return {"message": "Project updated"}