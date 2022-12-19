from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Deals(Base):
    __tablename__ = "deals"

    id = Column(String, primary_key=True, index=True)
    date = Column(String)
    funding_amount = Column(String)
    funding_round = Column(String)
    company_id = Column(Integer)

class Companies(Base):
    __tablename__ = "companies"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    founding_date = Column(String)
    description = Column(String)
    company_id = Column(Integer)