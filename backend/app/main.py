
from app.routes import router
from app.core.database import connect_to_db, disconnect_from_db
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import app.schemas.crypto  
import app.tasks.updater 

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Global Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error: {str(exc)}"}
    )

# Register startup and shutdown events
@app.on_event("startup")
async def startup():
    await connect_to_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_db()

# Include all CRUD routes
app.include_router(router)
