#### Project
from typing import Optional

import uvicorn
import yfinance
from fastapi import BackgroundTasks, Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy import engine
from sqlalchemy.orm import Session

from api import models

from .database import SessionLocal, engine
from .models import Stock
from .settings_handler import settings

app = FastAPI()


templates = Jinja2Templates(directory="templates")
models.Base.metadata.create_all(bind=engine)


class StockRequest(BaseModel):
    symbol: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def dashboard(
    request: Request,
    forward_pe=None,
    div_yield=None,
    ma50=None,
    ma200=None,
    db: Session = Depends(get_db),
):
    """
    ,
    """
    stocks = db.query(Stock)

    if forward_pe:
        stocks = stocks.filter(Stock.forward_pe > forward_pe)

    if div_yield:
        stocks = stocks.filter(Stock.div_yield > div_yield)

    if ma50:
        stocks = stocks.filter(Stock.price < ma50)

    if ma200:
        stocks = stocks.filter(Stock.price < ma200)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "stocks": stocks,
            "div_yield": div_yield,
            "forward_pe": forward_pe,
            "ma50": ma50,
            "ma200": ma200,
        },
    )


def fetch_stock_data(id: int):
    db = SessionLocal()
    stock = db.query(Stock).filter(Stock.id == id).first()

    yahoo_data = yfinance.Ticker(stock.symbol)
    stock.price = yahoo_data.info["previousClose"]
    stock.forward_eps = yahoo_data.info["forwardEps"]
    stock.ma200 = yahoo_data.info["twoHundredDayAverage"]
    stock.ma50 = yahoo_data.info["fiftyDayAverage"]

    if yahoo_data.info["forwardPE"]:
        stock.forward_pe = yahoo_data.info["forwardPE"]
    elif yahoo_data.info["forwardPE"] is None:
        stock.forward_pe = 0

    if yahoo_data.info["dividendYield"]:
        stock.div_yield = yahoo_data.info["dividendYield"] * 100
    elif yahoo_data.info["dividendYield"] is None:
        stock.div_yield = 0

    db.add(stock)
    db.commit()


@app.post("/stock")
async def create_stock(
    stock_request: StockRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    """
    add one or more tickers to the database
    background task to use yfinance and load key statistics
    """
    stock = Stock()
    stock.symbol = stock_request.symbol
    db.add(stock)
    db.commit()
    background_tasks.add_task(fetch_stock_data, stock.id)
    return {"code": "success", "message": "stock was added to the database"}


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
