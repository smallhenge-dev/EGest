from fastapi import FastAPI


app = FastAPI(
    title="EGest API",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Bienvenue sur l'API EGest"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
