from langchain_groq import ChatGroq
from graph.state import AgentState
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0)

def debug_agent_node(state: AgentState) -> AgentState:
    task = state["task"]
    context = state.get("code_context") or "No code provided."

    prompt = f"""You are an expert debugger. Analyze the error or bug described below.
Identify the root cause, explain why it happens, then provide the fixed code.

Problem: {task}
Code/Error: {context}"""

    response = llm.invoke(prompt)
    return {
        **state,
        "debug_result": response.content,
        "messages": state["messages"] + ["Debug agent completed."]
    }
