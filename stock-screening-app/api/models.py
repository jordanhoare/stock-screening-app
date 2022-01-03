from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import Numeric

from .database import Base


class Stock(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Integer[10, 2])
    forward_pe = Column(Integer[10, 2])
    forward_eps = Column(Integer[10, 2])
    div_yield = Column(Integer[10, 2])
    ma50 = Column(Numeric[10, 2])
    ma200 = Column(Numeric[10, 2])
