from sqlalchemy.orm import Session

from . import models
from . import schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_NFTs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.NFT).offset(skip).limit(limit).all()

def new_bid(db: Session, nft_id: int, amount: int, bidder: int):
    nft = db.query(models.NFT).filter(models.NFT.id == nft_id).first()
    nft.highest_bid = amount
    nft.user_bid = bidder
    db.commit()

def add_nft(db: Session, nft: models.NFT):
    db.add(nft)
    db.commit()