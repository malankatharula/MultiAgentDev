from langchain_groq import ChatGroq
from graph.state import AgentState
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0)

def test_agent_node(state: AgentState) -> AgentState:
    task = state["task"]
    context = state.get("code_context") or "No code provided."

    prompt = f"""You are a senior QA engineer. Write comprehensive pytest test cases.
Cover: happy path, edge cases, error cases. Use mocks where needed.

Task: {task}
Code: {context}"""

    response = llm.invoke(prompt)
    return {
        **state,
        "test_result": response.content,
        "messages": state["messages"] + ["Test agent completed."]
    }# Test agent implementation
