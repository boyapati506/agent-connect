from langgraph.types import interrupt
from app.graph.state import AgentState


def approval_node(state:AgentState):

    last_message = state["messages"][-1]

    approval = interrupt({
        "message": "Approval required before executing tool",
        "tool_calls": last_message.tool_calls,
    })

    return {
        "approval":approval
    }
