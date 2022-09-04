import json
from sqlalchemy.orm import Session
from src.sql_ops.func import SessionLocal
from src.sql_ops import models
import datetime

def get_db():
    dbCon = SessionLocal()
    try:
        yield dbCon
    finally:
        dbCon.close()

def import_fake_nfts(session: Session):
    nfts = json.load(open("fake_data.json", "r"))

    for nft in nfts:
        new = models.NFT()
        new.mint = datetime.datetime.strptime(nft['mint'], "%d-%m-%Y").date()
        new.company_name = nft['company_name']
        new.co2 = nft['co2']
        new.price = nft['price']
        new.retired = nft['retired']
        new.release = datetime.datetime.strptime(nft['release'], "%d-%m-%Y").date()
        new.technology = nft['technology']
        new.verification = nft['verification']
        new.highest_bid = 0
        session.add(new)
        session.commit()
