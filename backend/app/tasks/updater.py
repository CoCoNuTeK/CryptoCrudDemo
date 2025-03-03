from datetime import datetime
from app.schemas.crypto import Crypto
from app.services.coingecko import fetch_crypto_data
from app.core.scheduler import scheduler

async def fetch_and_update_all_cryptos():
    print("Fetching and updating all cryptos from CoinGecko...")
    cryptos = await Crypto.query.gino.all()
    print(f"Found {len(cryptos)} cryptocurrencies in the database.")

    for crypto in cryptos:
        print(f"Fetching data for {crypto.name}...")
        updated_data = await fetch_crypto_data(crypto.name)

        if updated_data:
            print(f"Updating {crypto.symbol} with data: {updated_data}")
            try:
                await Crypto.update.values(
                    current_price=updated_data.get("current_price"),
                    market_cap=updated_data.get("market_cap"),
                    last_updated=updated_data.get("last_updated", datetime.utcnow())
                ).where(Crypto.symbol == crypto.symbol).gino.status()
                print(f"Updated {crypto.symbol} successfully.")
            except Exception as e:
                print(f"Error updating {crypto.symbol}: {e}")
        else:
            print(f"No data to update for {crypto.symbol}.")

# Schedule the job to run every minute
scheduler.add_job(fetch_and_update_all_cryptos, 'interval', minutes=1)