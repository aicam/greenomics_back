import datetime

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import sys
sys.path.append('../../')
from src.sql_ops import schemas, crud, models
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

@router.get("/approve/nft")
def approve_nft(id: int, db: Session = Depends(get_db)):
    crud.approve_nft(db, id)
    return {"status": "Success"}
@router.post("/buy")
def add_owner(new_owner: schemas.NewOwner, db: Session = Depends(get_db)):
    res = crud.update_owner_by_ui(db, new_owner.owner, new_owner.nft_id, new_owner.stock)
    if not res:
        crud.add_nft_owner(db, new_owner.nft_id, new_owner.stock, new_owner.owner)
    return {"status": "Success"}

@router.post("/buy/off")
def buy_from_off(off_market: schemas.OffMarketBuy, db: Session = Depends(get_db)):
    crud.sell_off_market(db, off_market.owner, off_market.nft_id, off_market.stock)
    res = crud.update_owner_by_ui(db, off_market.buyer, off_market.nft_id, off_market.stock)
    if not res:
        crud.add_nft_owner(db, off_market.nft_id, off_market.stock, off_market.buyer)
    return {"status": "Success"}

@router.post("/add")
def add_nft(nft_info: schemas.AddedNFT, db: Session = Depends(get_db)):
    nft = models.NFT()
    nft.price = nft_info.price
    nft.mint = datetime.date.today()
    nft.release = nft_info.release
    nft.technology = nft_info.technology
    nft.co2 = nft_info.co2
    nft.verification = 0
    nft.added = "custom"
    nft.company_name = nft_info.company_name
    crud.add_nft(db, nft)
    return {"status": "Success"}