from langgraph.graph import StateGraph, END
from graph.state import AgentState
from graph.orchestrator import orchestrator_node
from graph.agents.code_agent import code_agent_node
from graph.agents.debug_agent import debug_agent_node
from graph.agents.doc_agent import doc_agent_node
from graph.agents.test_agent import test_agent_node

def route_to_agent(state: AgentState) -> str:
    return state["task_type"]  # returns "code", "debug", "doc", or "test"

def build_graph():
    graph = StateGraph(AgentState)

    # add all nodes
    graph.add_node("orchestrator", orchestrator_node)
    graph.add_node("code", code_agent_node)
    graph.add_node("debug", debug_agent_node)
    graph.add_node("doc", doc_agent_node)
    graph.add_node("test", test_agent_node)

    # entry point
    graph.set_entry_point("orchestrator")

    # orchestrator decides which agent to call
    graph.add_conditional_edges(
        "orchestrator",
        route_to_agent,
        {
            "code": "code",
            "debug": "debug",
            "doc": "doc",
            "test": "test"
        }
    )

    # all agents go to END after finishing
    graph.add_edge("code", END)
    graph.add_edge("debug", END)
    graph.add_edge("doc", END)
    graph.add_edge("test", END)

    return graph.compile()