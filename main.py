import httpx
import asyncio

async def get_posts():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://jsonplaceholder.typicode.com/posts")
        return res.json()

async def main():
    posts = await get_posts()
    for post in posts[:5]:
        
    
    titles = [p["title"] for p in posts if p["userId"] == 1]
    for t in titles[:5]:
        print(t)

asyncio.run(main())