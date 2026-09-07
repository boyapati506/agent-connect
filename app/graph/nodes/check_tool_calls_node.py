from app.graph.state import AgentState
from langgraph.graph import END

def checK_tool_calls_node(state:AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "approval"

    return END