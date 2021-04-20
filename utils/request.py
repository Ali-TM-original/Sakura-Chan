import aiohttp
from io import BytesIO



class req():
    def __init__(self):
        self.session = aiohttp.ClientSession(
                headers=None,
                timeout=aiohttp.ClientTimeout(total=60.0)
        )        

    async def magic(self, url: str) -> BytesIO:
        """MAGICAAA CONVERTS IMAGE TO BYTES."""

        async with self.session.get(url) as resp:

            data = await resp.read()

        return data

    async def yoda(self, text:str):
        param = {"text":text}
        async with self.session.get("http://yoda-api.appspot.com/api/v1/yodish", params=param) as resp:
            data = await resp.read()

        return data

    async def close(self) -> None:
        """Closes the Client."""
        return await self.session.close()
        