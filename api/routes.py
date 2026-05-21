from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from graph.graph_builder import build_graph

router = APIRouter()
agent_graph = build_graph()

class TaskRequest(BaseModel):
    task: str
    code_context: Optional[str] = None

class TaskResponse(BaseModel):
    task_type: str
    result: str
    messages: list

@router.post("/run", response_model=TaskResponse)
async def run_agent(request: TaskRequest):
    initial_state = {
        "task": request.task,
        "task_type": "",
        "code_context": request.code_context,
        "code_result": None,
        "debug_result": None,
        "doc_result": None,
        "test_result": None,
        "final_response": None,
        "messages": []
    }

    result = agent_graph.invoke(initial_state)

    # pick whichever result is populated
    task_type = result["task_type"]
    result_map = {
        "code": result.get("code_result"),
        "debug": result.get("debug_result"),
        "doc": result.get("doc_result"),
        "test": result.get("test_result"),
    }

    return TaskResponse(
        task_type=task_type,
        result=result_map.get(task_type, "No result."),
        messages=result["messages"]
    )# API routes
