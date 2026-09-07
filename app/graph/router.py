from langgraph.graph import END
from app.graph.state import AgentState

def route_after_approval(state : AgentState):
    last_message = state["messages"][-1]

    if state["approval"]:
          return "tools"

    return "rejected"
