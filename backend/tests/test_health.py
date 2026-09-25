import asyncio
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from fastapi.testclient import TestClient

from backend.app.api.route import route_student

from backend.app.main import app


def test_health_check() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_documentation_index() -> None:
    client = TestClient(app)

    response = client.get("/documentation")

    assert response.status_code == 200
    assert "Documentation EGest" in response.text
    assert "/assets/egestIcon.png" in response.text
    assert "/documentation/vision.md" in response.text


def test_documentation_page() -> None:
    client = TestClient(app)

    response = client.get("/documentation/vision.md")

    assert response.status_code == 200
    assert "Vision du Projet" in response.text


def test_database_module_imports_from_backend_package() -> None:
    from backend.app.database.database import Base

    assert Base is not None


def test_models_module_imports_from_backend_package() -> None:
    from backend.app.models.user import User

    assert User.__name__ == "User"


def test_sqlalchemy_model_relationship_registry_can_configure() -> None:
    import importlib
    import glob
    import sys

    sys.path.insert(0, ".")
    files = sorted(glob.glob("backend/app/models/*.py"))
    modules = [
        f.replace("\\", "/").replace(".py", "").replace("/", ".")
        for f in files
        if f != "backend/app/models/__init__.py"
    ]
    for module in modules:
        importlib.import_module(module)

    from backend.app.database.database import Base

    # Trigger SQLAlchemy relationship configuration and ensure the registry
    # can be resolved with no InvalidRequestErrors from back_populates.
    Base.registry.configure()

    assert len(Base.registry.mappers) >= 25


def test_logo_asset() -> None:
    client = TestClient(app)

    response = client.get("/assets/egestIcon.png")

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_student_route_uses_async_database_calls() -> None:
    async def run_test() -> None:
        mock_db = object()

        async def fake_read_list(db):
            assert db is mock_db
            return [{
                "id": 1,
                "user_id": None,
                "matricule": "E2024001",
                "first_name": "Alice",
                "last_name": "Martin",
                "date_of_birth": "2006-03-10",
                "place_of_birth": "Kinshasa",
                "gender": "F",
                "phone_number": None,
                "address": "1 rue de l'Université",
                "photo_url": None,
                "status": "active",
                "email": "alice.martin@egest.local",
                "is_active": True,
                "created_at": "2024-01-10T12:00:00",
                "updated_at": "2024-01-10T12:00:00",
            }]

        original_read_list = route_student.service_student.read_list
        route_student.service_student.read_list = fake_read_list
        try:
            result = await route_student.affiche_student(db=mock_db)
            assert result[0].first_name == "Alice"
            assert result[0].matricule == "E2024001"
        finally:
            route_student.service_student.read_list = original_read_list

    asyncio.run(run_test())


def test_update_student_rejects_duplicate_email() -> None:
    from backend.app.schemas.student import StudentUpdate

    class FakeScalarResult:
        def __init__(self, value):
            self.value = value

        def scalars(self):
            return self

        def first(self):
            return self.value

    class FakeSession:
        async def execute(self, stmt):
            if "WHERE students.id =" in str(stmt):
                return FakeScalarResult({"id": 2, "email": "alice.student@egest.local"})
            return FakeScalarResult({"id": 99, "email": "alice.student@egest.local"})

    async def run_test() -> None:
        db = FakeSession()
        payload = StudentUpdate(email="alice.student@egest.local")
        try:
            await route_student.service_student.update_student(db, 2, payload)
            assert False, "Une violation d'email dupliqué devrait être rejetée."
        except ValueError as exc:
            assert "email" in str(exc).lower()

    asyncio.run(run_test())


def test_delete_student_removes_linked_enrollments_before_parent() -> None:
    class FakeEnrollment:
        pass

    class FakeStudent:
        def __init__(self):
            self.enroll = [FakeEnrollment(), FakeEnrollment()]

    class FakeScalarResult:
        def __init__(self, value):
            self.value = value

        def scalars(self):
            return self

        def first(self):
            return self.value

        def all(self):
            return self.value

    class FakeSession:
        def __init__(self, student):
            self.student = student
            self.deleted = []

        async def execute(self, stmt):
            if "enrollments" in str(stmt):
                return FakeScalarResult(self.student.enroll)
            return FakeScalarResult(self.student)

        async def delete(self, obj):
            self.deleted.append(obj)

        async def commit(self):
            return None

    async def run_test() -> None:
        student = FakeStudent()
        db = FakeSession(student)
        result = await route_student.service_student.delete_student(db, 42)
        assert result is student
        assert len(db.deleted) == 3
        assert all(obj in db.deleted for obj in student.enroll)
        assert db.deleted[-1] is student

    asyncio.run(run_test())


def test_main_module_starts_fastapi_server_for_swagger() -> None:
    project_root = Path(__file__).resolve().parents[2]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)

    process = subprocess.Popen(
        [sys.executable, "backend/app/main.py"],
        cwd=str(project_root),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    try:
        for _ in range(20):
            time.sleep(0.5)
            try:
                with urllib.request.urlopen("http://127.0.0.1:8000/docs", timeout=2) as response:
                    assert response.status == 200
                    break
            except Exception:
                if process.poll() is not None:
                    stdout, stderr = process.communicate(timeout=2)
                    raise AssertionError(f"Le script a terminé avant de démarrer le serveur.\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")
        else:
            raise AssertionError("Swagger /docs n'est pas accessible après démarrage du script main.py")
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
