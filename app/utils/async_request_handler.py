import aiohttp
from app.config import NEWS_API_URL, NEWS_API_KEY


class AsyncRequestHandler:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {NEWS_API_KEY}"}

    async def get(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.get(NEWS_API_URL, headers=self.headers) as response:
                data = await response.json()
                return data

    async def post(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                NEWS_API_URL, headers=self.headers, data=data
            ) as response:
                data = await response.json()
                return data
