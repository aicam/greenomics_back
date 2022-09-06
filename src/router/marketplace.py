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

@router.get("/owners")
def get_owners_list(db: Session = Depends(get_db)):
    return crud.get_all_owners(db)

@router.get("/retire")
def retire(id: int, db: Session = Depends(get_db)):
    crud.retire(db, id)
    return {"status": "Success"}

@router.get("/sell")
def sell(id: int, amount: float, price: float, db: Session = Depends(get_db)):
    crud.add_selling_stock(db, id, amount, price)
    return {"status": "Success"}

@router.get("/cancel/selling")
def cancel_selling(id: int, db: Session = Depends(get_db)):
    crud.cancel_selling_stock(db, id)
    return {"status": "Success"}
@router.post("/buy")
def add_owner(new_owner: schemas.NewOwner, db: Session = Depends(get_db)):
    res = crud.update_owner_by_ui(db, new_owner.owner, new_owner.nft_id, new_owner.stock)
    if not res:
        crud.add_nft_owner(db, new_owner.nft_id, new_owner.stock, new_owner.owner)
    return {"status": "Success"}

