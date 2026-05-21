from langchain_groq import ChatGroq
from graph.state import AgentState
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0)

def doc_agent_node(state: AgentState) -> AgentState:
    task = state["task"]
    context = state.get("code_context") or "No code provided."

    prompt = f"""You are a technical writer. Generate clear, professional documentation.
Include: overview, parameters/inputs, outputs, usage example.

Task: {task}
Code: {context}"""

    response = llm.invoke(prompt)
    return {
        **state,
        "doc_result": response.content,
        "messages": state["messages"] + ["Doc agent completed."]
    }
