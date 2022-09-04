from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from func import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(30), unique=True, index=True)
    hashed_password = Column(String(50))
    name = Column(String(20))
    address = Column(String(50))
    phonenumber = Column(String(20))
    career = Column(String(20))
    license_number = Column(String(30))
    certificate = Column(String(100))
    balance = Column(Float)
    token = Column(Float)

class NFT(Base):
    __tablename__ = "nft"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(30))
    co2 = Column(Float)
    technology = Column(String(30))
    verification = Column(Integer)
    price = Column(Float)
    release = Column(Date)
    mint = Column(Date)
    highest_bid = Column(Float)
    user_bid = Column(Integer)
    retired = Column(Boolean)

class NFTOwners(Base):
    __tablename__ = "nft_owners"

    id = Column(Integer, primary_key=True, index=True)
    nft_id = Column(Integer)
    owner = Column(String(30))
    stake = Column(Float)

