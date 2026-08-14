from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.app.api.route.documentation import router as documentation_router


ASSETS_DIRECTORY = "frontend/app/assets"

app = FastAPI(
    title="EGest API",
    version="0.1.0",
)

app.mount("/assets", StaticFiles(directory=ASSETS_DIRECTORY), name="assets")
app.include_router(documentation_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Bienvenue sur l'API EGest"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
