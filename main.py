from fastapi import FastAPI
from src.sql_ops import models, crud
from src.sql_ops.func import engine
from fastapi.middleware.cors import CORSMiddleware
from helper import import_fake_nfts
from src.router import marketplace
from src.sql_ops.func import SessionLocal

models.Base.metadata.create_all(engine)
if len(crud.get_NFTs(SessionLocal())) == 0:
    import_fake_nfts(SessionLocal())

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(marketplace.router)