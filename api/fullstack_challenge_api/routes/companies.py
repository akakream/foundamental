from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from sqlalchemy.orm import Session
from .models import Companies, Deals

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
    return db.query(Companies).all()

@router.get("/deals")
async def get_deals(db: Session = Depends(get_db)):
    return db.query(Deals).all()

@router.get("/companiesWithDeals")
async def get_companiesWithDeals(db: Session = Depends(get_db)):
    query_result = db.query(Companies, Deals).join(Deals, Companies.id == Deals.company_id, isouter=True).all()

    result = {}
    for pair in query_result:
        company_key = pair["Companies"].id
        if company_key not in result:
            result[company_key] = {}
            result[company_key]["Company"] = pair["Companies"]
            result[company_key]["Deals"] = [pair["Deals"]]
        else:
            result[company_key]["Deals"].append(pair["Deals"])

    return result