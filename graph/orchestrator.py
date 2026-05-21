from langchain_groq import ChatGroq
from graph.state import AgentState
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

def orchestrator_node(state: AgentState) -> AgentState:
    task = state["task"]

    prompt = f"""You are a routing agent. Given a developer task, classify it into exactly one of these categories:
- code → user wants code written or explained
- debug → user has an error or bug to fix
- doc → user wants documentation generated
- test → user wants test cases written

Task: {task}

Reply with only one word: code, debug, doc, or test."""

    response = llm.invoke(prompt)
    task_type = response.content.strip().lower()

    # fallback if model hallucinates
    if task_type not in ["code", "debug", "doc", "test"]:
        task_type = "code"

    return {
        **state,
        "task_type": task_type,
        "messages": state["messages"] + [f"Orchestrator routed to: {task_type}"]
    }# Orchestrator for managing agent workflows
