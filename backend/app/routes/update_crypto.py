from fastapi import APIRouter, HTTPException
from app.schemas.crypto import Crypto
from app.schemas.request import CryptoUpdateRequest

router = APIRouter()

@router.put("/update_crypto", response_model=dict)
async def update_crypto(update_data: CryptoUpdateRequest):
    
    crypto = await Crypto.query.where(Crypto.symbol == update_data.symbol).gino.first()
    if not crypto:
        raise HTTPException(status_code=404, detail="Cryptocurrency not found")

    await crypto.update(description=update_data.description).apply()

    return {"message": f"Cryptocurrency with symbol '{update_data.symbol}' updated successfully"}
