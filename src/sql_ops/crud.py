from sqlalchemy.orm import Session
from datetime import date
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
    new_nft_owner.bought_date = date.today()
    db.add(new_nft_owner)
    return db.commit()

def get_stock_by_id(db: Session, stock_id: int):
    return db.query(models.NFTOwners).filter(models.NFTOwners.id == stock_id).first()

def add_selling_stock(db: Session, stock_id: int, stock: float, price: float):
    NFTOwner = db.query(models.NFTOwners).filter(models.NFTOwners.id == stock_id).first()
    NFTOwner.stock += NFTOwner.selling_stock - stock
    NFTOwner.selling_stock = stock
    NFTOwner.selling_price = price
    return db.commit()
def cancel_selling_stock(db: Session, stock_id: int):
    NFTOwner = db.query(models.NFTOwners).filter(models.NFTOwners.id == stock_id).first()
    NFTOwner.stock += NFTOwner.selling_stock
    NFTOwner.selling_stock = 0
    NFTOwner.selling_price = 0
    return db.commit()
def remove_stock(db: Session, stock_id: int):
    row = db.query(models.NFTOwners).filter(models.NFTOwners.id == stock_id).first()
    db.delete(row)
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

def update_owner_by_ui(db: Session, username: str, nft_id: int, stock: float):
    nft_owner = db.query(models.NFTOwners).filter(models.NFTOwners.nft_id == nft_id,
                                                  models.NFTOwners.owner == username,
                                                  models.NFTOwners.retired == False).first()
    if nft_owner == None:
        return False
    nft_owner.stock += stock
    db.commit()
    return True

def sell_off_market(db: Session, username: str, nft_id: int, stock: float):
    nft_owner = db.query(models.NFTOwners).filter(models.NFTOwners.nft_id == nft_id,
                                                  models.NFTOwners.owner == username,
                                                  models.NFTOwners.retired == False).first()
    nft_owner.selling_stock -= stock
    if nft_owner.selling_stock == 0 and nft_owner.stock == 0:
        db.delete(nft_owner)
    db.commit()

def approve_nft(db: Session, nft_id: int):
    nft = db.query(models.NFT).filter(models.NFT.id == nft_id).first()
    nft.verification += 1
    db.commit()