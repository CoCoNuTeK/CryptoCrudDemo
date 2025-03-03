from gino import Gino
from app.core.config import settings
from .scheduler import start_scheduler, shutdown_scheduler

db = Gino()

async def connect_to_db():
    print("Connecting to the database...")
    await db.set_bind(settings.DATABASE_URL)
    
    print("Dropping all tables...")
    await db.gino.drop_all()
    
    print("Creating database tables if they do not exist...")
    await db.gino.create_all()
    print("Tables creation check completed.")
    print("Connected to the database.")

    start_scheduler()

async def disconnect_from_db():
    
    shutdown_scheduler()

    print("Disconnecting from the database...")
    await db.pop_bind().close()
    print("Disconnected from the database.")


