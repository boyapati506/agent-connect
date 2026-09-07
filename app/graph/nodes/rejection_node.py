from langchain_core.messages import ToolMessage
from app.graph.state import AgentState


def rejection_node(state: AgentState):

    last_message = state["messages"][-1]

    tool_messages = []

    for tool_call in last_message.tool_calls:
        tool_messages.append(
            ToolMessage(
                content= "Tool execution was rejected for this request only. "
                    "If the user makes a new request requiring this tool, "
                    "the tool may be requested again and a new approval "
                    "must be obtained.",
                tool_call_id=tool_call["id"]
            )
        )

    return {
        "messages": tool_messages
    }