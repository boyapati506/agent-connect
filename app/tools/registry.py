from langchain_core.tools import BaseTool

class ToolRegistry:

    def __init__(self):
        self.__tools:dict[str,BaseTool] = {}

    def register(self,tool:BaseTool) -> None :
        self.__tools[tool.name] = tool

    def get(self,name:str) -> BaseTool:

        tool = self.__tools.get(name)

        if tool is None:
            raise ValueError(f"Tool not found : {name}")

        return tool

    def get_all(self) -> list[BaseTool]:
        return list(self.__tools.values())