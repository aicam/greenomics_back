from pydantic import BaseModel

class NewOwner(BaseModel):
    owner: str
    nft_id: int
    stock: float