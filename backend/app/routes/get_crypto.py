from fastapi import APIRouter, HTTPException
from app.schemas.crypto import Crypto
from app.schemas.request import CryptoResponse

router = APIRouter()

@router.get("/get_crypto/{symbol}", response_model=CryptoResponse)
async def get_crypto(symbol: str):
    
    crypto = await Crypto.query.where(Crypto.symbol == symbol).gino.first()
    
    if not crypto:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
    
    return CryptoResponse(**crypto.to_dict())

