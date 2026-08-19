from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home() -> dict[str, Any]:
    return {"Hello": "World"}
