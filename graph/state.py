# State managemenfrom typing import TypedDict, List, Optional
from typing import TypedDict, List, Optional
class AgentState(TypedDict):
    task: str                          # original user task
    task_type: str                     # what orchestrator decides: code / debug / doc / test
    code_context: Optional[str]        # any code user pastes in
    code_result: Optional[str]         # output from code agent
    debug_result: Optional[str]        # output from debug agent
    doc_result: Optional[str]          # output from doc agent
    test_result: Optional[str]         # output from test agent
    final_response: Optional[str]      # aggregated final answer
    messages: List[str]                # running log of what happenedt for the agent graph
