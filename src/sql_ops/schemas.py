from pydantic import BaseModel

class NewOwner(BaseModel):
    owner: str
    nft_id: int
    stock: float

class OffMarketBuy(BaseModel):
    buyer: str
    nft_id: int
    stock: float
    owner: str