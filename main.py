from fastapi import FastAPI
from pydantic import BaseModel

from services.ai import ask_ai

app = FastAPI()


class ResearchRequest(BaseModel):
    query: str


@app.get("/")
async def root():
    return {"message": "AI Research Assistant API"}


@app.post("/research")
async def research(data: ResearchRequest):

    result = await ask_ai(data.query)

    return result