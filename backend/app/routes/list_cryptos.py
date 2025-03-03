from fastapi import APIRouter
from app.schemas.crypto import Crypto
from app.schemas.request import CryptoResponse

router = APIRouter()

@router.get("/list", response_model=list[CryptoResponse])
async def list_cryptos():
    
    cryptos = await Crypto.query.gino.all()
    
    return [CryptoResponse(**crypto.to_dict()) for crypto in cryptos]
