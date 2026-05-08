import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


async def ask_ai(query: str):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": "baidu/cobuddy:free",
        "messages": [
            {
                "role": "user",
                "content": f"""
                Give short research summary about:
                {query}

                Return:
                - short summary
                - 3 key points
                """
            }
        ]
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=json_data
        )

        return response.json()