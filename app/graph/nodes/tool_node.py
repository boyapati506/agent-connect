from langchain_core.messages import ToolMessage
from app.tools.registry import ToolRegistry
from app.graph.state import AgentState

def build_tool_node(tool_registry : ToolRegistry):
    def tool_node(state : AgentState):

        last_message = state["messages"][-1]

        tool_messages=[]

        for tool_call in last_message.tool_calls:

            try:
                tool = tool_registry.get(tool_call["name"])
                result = tool.invoke(tool_call["args"])
                tool_messages.append(ToolMessage(
                    content=str(result),
                    tool_call_id = tool_call["id"]
                ))
            except Exception as ex:
                  tool_message = ToolMessage(
                                             content=f"Tool execution failed: {str(ex)}",
                                             tool_call_id=tool_call["id"]
                                         )
        return {"messages":tool_messages}
    return tool_node
