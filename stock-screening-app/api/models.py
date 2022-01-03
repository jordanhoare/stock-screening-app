from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import Numeric

from database import Base


class User(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    price = Column(Numeric[10, 2])
    foward_pe = Column(Numeric[10, 2])
    foward_eps = Column(Numeric[10, 2])
    div_yield = Column(Numeric[10, 2])
    ma50 = Column(Numeric[10, 2])
    ma200 = Column(Numeric[10, 2])
