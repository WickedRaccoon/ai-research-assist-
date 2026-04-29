import httpx
import asyncio

async def get_posts():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get("https://jsonplaceholder.typicode.com/posts")
            if res.status_code != 200:
                print("Error")
                return []
            return res.json()
    except Exception:
        print("Error: failed to fetch posts")
        return []

async def main():
    posts = await get_posts()
    
    # Группируем посты по userId
    posts_by_user = {}
    for post in posts:
        user_id = post["userId"]
        if user_id not in posts_by_user:
            posts_by_user[user_id] = []
        posts_by_user[user_id].append(post)
    
    # Выводим результат
    for user_id in sorted(posts_by_user.keys()):
        user_posts = posts_by_user[user_id]
        titles = [p["title"] for p in user_posts[:3]]
        
        print(f"User {user_id}:")
        print(f"  posts: {len(user_posts)}")
        print(f"  titles:")
        for title in titles:
            print(f"    - {title}")
        print()

asyncio.run(main())

