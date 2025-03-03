from pydantic import BaseModel, Field
from datetime import datetime

class CryptoBase(BaseModel):
    symbol: str = Field(..., description="Symbol of the cryptocurrency", example="btc")
    name: str = Field(None, description="Name of the cryptocurrency", example="Bitcoin")
    current_price: float = Field(None, description="Current price of the cryptocurrency", example=50000.0)
    market_cap: float = Field(None, description="Market capitalization of the cryptocurrency", example=800000000.0)
    market_cap_rank: int = Field(None, description="Market cap rank of the cryptocurrency", example=1)
    description: str = Field(None, description="Description of the cryptocurrency", example="A decentralized digital currency.")
    last_updated: datetime | None = Field(None, description="Last updated timestamp", example="2023-08-25T12:34:56Z")

class CryptoCreateRequest(CryptoBase):
    pass

class CryptoResponse(CryptoBase):
    id: int = Field(..., description="ID of the cryptocurrency", example=1)

class CryptoUpdateRequest(BaseModel):
    symbol: str = Field(..., description="Symbol of the cryptocurrency to update", example="btc")
    description: str = Field(..., description="New description of the cryptocurrency", example="An updated description for the cryptocurrency.")

class CryptoSymbolRequest(BaseModel):
    symbol: str = Field(..., description="Symbol of the cryptocurrency", example="btc")