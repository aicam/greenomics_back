from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import sys
sys.path.append('../../')
from src.sql_ops import schemas, crud
from helper import get_db

router = APIRouter(
    prefix="/marketplace"
)

@router.get("/nft_list")
def get_nfts(db: Session = Depends(get_db)):
    return crud.get_NFTs(db)