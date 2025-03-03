import httpx
from datetime import datetime

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

async def check_crypto_exists(symbol: str) -> bool:
    """
    Check if a cryptocurrency exists on CoinGecko by symbol.
    """
    url = f"{COINGECKO_API_URL}/coins/list"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            cryptos = response.json()

        # Log the total number of cryptos fetched and a sample of the data
        print(f"Fetched {len(cryptos)} cryptos from CoinGecko for validation.")
        print(f"Sample data from CoinGecko: {cryptos[:5]}")

        # Check if the symbol exists
        found = False
        possible_matches = []

        for crypto in cryptos:
            if crypto["symbol"].lower() == symbol.lower():
                print(f"Symbol {symbol} found on CoinGecko with ID: {crypto['id']}")
                found = True
                break
            if symbol.lower() in crypto["symbol"].lower():
                possible_matches.append(crypto["symbol"])

        if not found:
            print(f"Symbol {symbol} not found on CoinGecko.")
            print(f"Possible close matches: {possible_matches}")

        return found

    except httpx.HTTPError as e:
        print(f"Failed to fetch data from CoinGecko: {e}")
        return False


async def fetch_crypto_data(crypto_name: str) -> dict:
    url = f"{COINGECKO_API_URL}/simple/price"
    params = {
        "ids": crypto_name.lower(),
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true",
        "include_last_updated_at": "true"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            market_data = response.json()

            print(f"Market data fetched for {crypto_name}: {market_data}")

            if market_data and crypto_name.lower() in market_data:
                result = {
                    "current_price": market_data[crypto_name.lower()].get("usd"),
                    "market_cap": market_data[crypto_name.lower()].get("usd_market_cap"),
                    "last_updated": datetime.utcfromtimestamp(
                        market_data[crypto_name.lower()].get("last_updated_at") or 0
                    )
                }
                print(f"Processed market data for {crypto_name}: {result}")
                return result

            print(f"No valid market data returned for {crypto_name}")

    except httpx.HTTPError as e:
        print(f"Failed to fetch data for {crypto_name}: {e}")
    return {}