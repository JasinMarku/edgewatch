from fastapi import FastAPI

from app import __version__

app = FastAPI(title="EdgeWatch", version=__version__)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
