import openai
import asyncio
import os
from tools.query_mysql import get_documents_summary

openai.api_key = "dummy"  # Required by client
openai.base_url = "http://localhost:11434/v1"

functions = [
    {
        "name": "get_documents_summary",
        "description": "Fetch and summarize registry documents by date range",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {"type": "string"},
                "end_date": {"type": "string"},
            },
            "required": ["start_date", "end_date"]
        }
    }
]

async def run_agent(query: str):
    response = await openai.ChatCompletion.acreate(
        model="qwen:0.5b",  # Make sure this model is running via Ollama
        messages=[
            {"role": "user", "content": query}
        ],
        functions=functions,
        function_call="auto"
    )

    message = response["choices"][0]["message"]
    if message.get("function_call"):
        name = message["function_call"]["name"]
        args = eval(message["function_call"]["arguments"])

        if name == "get_documents_summary":
            result = await get_documents_summary(**args)
            return result

    return message["content"]