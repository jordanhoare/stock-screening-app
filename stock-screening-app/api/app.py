#### Project
from typing import Optional

import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import engine

from db import database, models

from .settings_handler import settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def dashboard(request: Request):
    """
    ,
    """
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "somevar": 2,
        },
    )


@app.post("/stock")
async def create_stock():
    """
    ,
    """
    return {
        "code": "success",
        "message": "stock created",
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


#### Run app
def run():
    """Run the API using Uvicorn"""
    """https://github.com/David-Lor/FastAPI-Template/tree/master/my_api/settings_handler"""
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
    )


__all__ = ("app", "run")


if __name__ == "__main__":
    run()
