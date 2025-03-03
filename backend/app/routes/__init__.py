from fastapi import APIRouter
from app.routes.create_crypto import router as create_crypto_router
from app.routes.get_crypto import router as get_crypto_router
from app.routes.list_cryptos import router as list_cryptos_router
from app.routes.update_crypto import router as update_crypto_router
from app.routes.delete_crypto import router as delete_crypto_router

router = APIRouter()

router.include_router(create_crypto_router, prefix="/cryptos", tags=["Create Crypto"])
router.include_router(list_cryptos_router, prefix="/cryptos", tags=["List Cryptos"])
router.include_router(get_crypto_router, prefix="/cryptos", tags=["Get Crypto"])
router.include_router(update_crypto_router, prefix="/cryptos", tags=["Update Crypto"])
router.include_router(delete_crypto_router, prefix="/cryptos", tags=["Delete Crypto"])
