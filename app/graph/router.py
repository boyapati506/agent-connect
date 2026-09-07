from langgraph.graph import END
from app.graph.state import AgentState

def route_after_agent(state : AgentState):
    last_message = state["messages"][-1]

    if  last_message.tool_calls:
          return "tools"

    return END
