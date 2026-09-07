from app.graph.state import AgentState
from langchain_core.language_models.chat_models import BaseChatModel

def build_agent_node(model_with_tool:BaseChatModel):
    def agent_node(state:AgentState) -> AgentState:
        response = model_with_tool.invoke(
            state["messages"]
        )
        return {"messages":response}
    return agent_node
