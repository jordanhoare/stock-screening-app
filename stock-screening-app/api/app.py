from typing import Optional

import uvicorn
from fastapi import FastAPI

from .settings_handler import settings

app = FastAPI()


@app.get("/")
async def read_root():
    """https://fastapi.tiangolo.com/"""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


def run():
    """Run the API using Uvicorn"""
    """https://github.com/David-Lor/FastAPI-Template/tree/master/my_api/settings_handler"""
    uvicorn.run(
        app, host=settings.host, port=settings.port, log_level=settings.log_level
    )


__all__ = ("app", "run")


if __name__ == "__main__":
    run()
