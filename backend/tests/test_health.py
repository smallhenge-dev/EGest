from fastapi.testclient import TestClient

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


def test_logo_asset() -> None:
    client = TestClient(app)

    response = client.get("/assets/egestIcon.png")

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
