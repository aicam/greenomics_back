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

def add_nft_owner(db: Session, nft_id: int, stock: float, owner: str):
    new_nft_owner = models.NFTOwners()
    new_nft_owner.owner = owner
    new_nft_owner.nft_id = nft_id
    new_nft_owner.stock = stock
    new_nft_owner.retired = False
    db.add(new_nft_owner)
    return db.commit()

def get_all_owners(db: Session):
    return db.query(models.NFTOwners).all()

def retire(db: Session, nft_owner_id: int):
    no = db.query(models.NFTOwners).filter(models.NFTOwners.id == nft_owner_id).first()
    no.retired = True
    db.commit()
def add_nft(db: Session, nft: models.NFT):
    db.add(nft)
    db.commit()