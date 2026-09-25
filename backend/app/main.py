from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

if __package__ in {None, ""}:
    project_root = Path(__file__).resolve().parents[2]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

ASSETS_DIRECTORY = str((Path(__file__).resolve().parents[2] / "frontend" / "app" / "assets").resolve())

from importlib import import_module

for module_name in [
    "academic_level",
    "attendance",
    "attendance_session",
    "audit_logs",
    "class_sub",
    "classe",
    "document",
    "enrollment",
    "fee",
    "grade",
    "invoice",
    "invoice_item",
    "message",
    "notification",
    "parent",
    "parent_student",
    "payment",
    "report",
    "schedule",
    "school_year",
    "student",
    "subject",
    "teacher",
    "teacher_sub",
    "term",
    "user",
]:
    import_module(f"backend.app.models.{module_name}")

from backend.app.api.route.documentation import router as documentation_router
from backend.app.schemas.student import StudentCreate
from backend.app.api.route.route_student import route as student_router

app = FastAPI(
    title="EGest API",
    version="0.1.0",
)

app.mount("/assets", StaticFiles(directory=ASSETS_DIRECTORY), name="assets")
app.include_router(documentation_router)
app.include_router(student_router)

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Bienvenue sur l'API EGest"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/student")
async def get_student(student: StudentCreate):
    return {"message":"etudiant enregistree avec succes", "reponse":student}
 