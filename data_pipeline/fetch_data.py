import aiohttp
import asyncio
import aiofiles
from datetime import datetime

API_URL = "https://www.federalregister.gov/api/v1/documents.json"

async def fetch_data():
    params = {
        "per_page": 20,
        "order": "newest",
        "conditions[publication_date][gte]": "2025-01-01"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL, params=params) as resp:
            data = await resp.json()
            async with aiofiles.open("data_pipeline/raw_data.json", "w") as f:
                await f.write(str(data))

asyncio.run(fetch_data())