# Import FastAPI framework for building the web API
from fastapi import FastAPI

# Import BaseModel from Pydantic for request data validation
from pydantic import BaseModel

# Import the agent logic (assumed to be async) from your agent module
from agent.agent import run_agent

# Import uvicorn server (used to run the FastAPI app)
import uvicorn

# Create an instance of the FastAPI application
app = FastAPI()

# Define the expected request body format using Pydantic
class QueryRequest(BaseModel):
    query: str  # The user's query as a string

# Define a POST endpoint at /chat
@app.post("/chat")
async def chat(req: QueryRequest):
    # Call the agent with the user's query and wait for the response
    response = await run_agent(req.query)

    # Return the response in a JSON object
    return {"response": response}
