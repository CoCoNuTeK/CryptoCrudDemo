from fastapi import APIRouter, HTTPException
from app.schemas.crypto import Crypto
from app.schemas.request import CryptoCreateRequest
from app.services.coingecko import check_crypto_exists, fetch_crypto_data
from datetime import datetime

router = APIRouter()

@router.post("/create_crypto", response_model=dict)
async def create_crypto(crypto: CryptoCreateRequest):
    # Check if the symbol already exists in the database
    existing_crypto = await Crypto.query.where(Crypto.symbol == crypto.symbol).gino.first()
    if existing_crypto:
        raise HTTPException(status_code=400, detail="Cryptocurrency with this symbol already exists in the database")
    
    # Check if the cryptocurrency symbol exists on CoinGecko
    symbol_exists = await check_crypto_exists(crypto.symbol)
    if not symbol_exists:
        raise HTTPException(status_code=404, detail="Cryptocurrency symbol not found on CoinGecko")

    # Insert the new cryptocurrency record into the database
    new_crypto = await Crypto.create(**crypto.dict())
    
    # Fetch market data immediately to update the new record
    updated_data = await fetch_crypto_data(crypto.name)
    if updated_data:
        await Crypto.update.values(
            current_price=updated_data.get("current_price"),
            market_cap=updated_data.get("market_cap"),
            last_updated=datetime.utcnow()
        ).where(Crypto.symbol == crypto.symbol).gino.status()

    return {"message": "Cryptocurrency created successfully", "symbol": crypto.symbol}
