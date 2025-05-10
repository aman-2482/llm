from fastapi import FastAPI
from pydantic import BaseModel
from agent.agent import run_agent
import uvicorn

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/chat")
async def chat(req: QueryRequest):
    response = await run_agent(req.query)
    return {"response": response}