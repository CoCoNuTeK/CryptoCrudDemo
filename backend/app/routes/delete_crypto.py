from fastapi import APIRouter, HTTPException
from app.schemas.crypto import Crypto
from app.schemas.request import CryptoSymbolRequest

router = APIRouter()

@router.delete("/delete_crypto", response_model=dict)
async def delete_crypto(request: CryptoSymbolRequest):
    
    crypto = await Crypto.query.where(Crypto.symbol == request.symbol).gino.first()
    if not crypto:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")
  
    await crypto.delete()

    return {"message": "Cryptocurrency deleted successfully", "symbol": request.symbol}
