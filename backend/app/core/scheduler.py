from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Create one global AsyncIOScheduler instance
scheduler = AsyncIOScheduler()

def start_scheduler():
    """Start the APScheduler."""
    scheduler.start()

def shutdown_scheduler():
    """Shut down the APScheduler gracefully."""
    print("Shutting down the scheduler...")
    scheduler.shutdown()
