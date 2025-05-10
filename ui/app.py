import gradio as gr
import requests

API_URL = "http://localhost:8000/chat"

def ask_agent(user_input):
    response = requests.post(API_URL, json={"query": user_input})
    return response.json().get("response", "No response")

gr.Interface(fn=ask_agent, inputs="text", outputs="text", title="RAG Chat Agent").launch()