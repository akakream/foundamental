from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from sqlalchemy.orm import Session
from .models import Companies, Deals

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
    return db.query(Companies).offset(0).limit(10000).all()
    pass

@router.get("/deals")
async def get_deals(db: Session = Depends(get_db)):
    return db.query(Deals).offset(0).limit(10000).all()
    pass