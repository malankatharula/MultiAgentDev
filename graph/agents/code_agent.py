from langchain_groq import ChatGroq
from graph.state import AgentState
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0)

def code_agent_node(state: AgentState) -> AgentState:
    task = state["task"]
    context = state.get("code_context") or "No additional code provided."

    prompt = f"""You are an expert software engineer. Write clean, production-grade code for the following task.
Include comments. Explain briefly what the code does after.

Task: {task}
Context/Existing Code: {context}"""

    response = llm.invoke(prompt)
    return {
        **state,
        "code_result": response.content,
        "messages": state["messages"] + ["Code agent completed."]
    }
