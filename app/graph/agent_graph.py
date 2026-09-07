from app.graph.nodes.tool_node import build_tool_node
from app.graph.nodes.agent_node import build_agent_node
from langgraph.graph import StateGraph,START,END
from app.graph.router import route_after_approval 
from app.graph.state import AgentState
from app.tools.registry import ToolRegistry
from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.checkpoint.memory import InMemorySaver
from app.graph.nodes.approval_node import approval_node
from app.graph.nodes.check_tool_calls_node import checK_tool_calls_node
from app.graph.nodes.rejection_node import rejection_node
from langgraph.checkpoint.postgres import PostgresSaver
from app.db.database import LANGGRAPH_DATABASE_URL



#check_pointer = InMemorySaver()

def build_agent_graph(
        tool_registry: ToolRegistry,
        model_with_tool : BaseChatModel,
         check_pointer
):
  
        graph =  StateGraph(AgentState)
        agent_node = build_agent_node(model_with_tool=model_with_tool)
        tool_node = build_tool_node(tool_registry=tool_registry)
        graph.add_node("agent",agent_node)
        graph.add_node("tools",tool_node)
        graph.add_node("approval",approval_node)
        graph.add_node("check_tool_call",checK_tool_calls_node)
        graph.add_node("rejected",rejection_node)

        graph.add_edge(START,"agent")
        graph.add_conditional_edges(
            "agent",
            checK_tool_calls_node
        )
        graph.add_conditional_edges(
            "approval",
            route_after_approval
        )
        graph.add_edge("tools","agent")
        graph.add_edge("rejected","agent")

        return graph.compile(
            checkpointer=check_pointer
        )    