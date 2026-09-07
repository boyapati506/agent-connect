from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from app.prompts.loader import load_system_prompt
from app.llm.schemas.agent_decision import AgentDecision
from app.tools.registry import ToolRegistry
from langchain_core.messages import ToolMessage


class LLMService:

    def __init__(self,model:BaseChatModel,tool_registry : ToolRegistry):
        self.tool_registry = tool_registry
        tools = tool_registry.get_all()
        self.model_with_tools = model.bind_tools(tools)
        self.model_with_structured_output = model.with_structured_output(AgentDecision) 
        
        self.prompt =  ChatPromptTemplate.from_messages([
            ("system",load_system_prompt()),
            ("human","{user_input}"),
            MessagesPlaceholder("agent_messages")
        ])
        self.llm_chain = self.prompt | self.model_with_tools

    def ask(self,user_input:str) :

        agent_messages =[]
       
        llm_response=self.llm_chain.invoke({
            "user_input": user_input,
            "agent_messages":[]
        })

        if not llm_response.tool_calls:
            return llm_response.content


        agent_messages.append(llm_response)

        for tool_call in llm_response.tool_calls:

            tool = self.tool_registry.get(tool_call["name"])

            result = tool.invoke(tool_call["args"])

            agent_messages.append(ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            ))

            print(agent_messages)
        final_response = self.llm_chain.invoke({
              "user_input": user_input,
                "agent_messages": agent_messages
        })
        return final_response.content
      

       