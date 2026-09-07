from app.graph.nodes.tool_node import build_tool_node
from app.graph.nodes.agent_node import build_agent_node
from langgraph.graph import StateGraph,START
from app.graph.router import route_after_agent 
from app.graph.state import AgentState
from app.tools.registry import ToolRegistry
from langchain_core.language_models.chat_models import BaseChatModel

def build_agent_graph(
        tool_registry: ToolRegistry,
        model_with_tool : BaseChatModel
):
    graph =  StateGraph(AgentState)
    agent_node = build_agent_node(model_with_tool=model_with_tool)
    tool_node = build_tool_node(tool_registry=tool_registry)
    graph.add_node("agent",agent_node)
    graph.add_node("tools",tool_node)

    graph.add_edge(START,"agent")
    graph.add_conditional_edges(
        "agent",
        route_after_agent
    )
    graph.add_edge("tools","agent")
    return graph.compile()    