import yaml
from pathlib import Path
from typing import Dict, Any, List
from langchain.tools import Tool, BaseTool
from langchain.agents import Tool as AgentTool
from langchain.tools import BaseTool
from langchain.tools.base import ToolException
from ..tools.summarizer import SummarizerTool

class ToolManager:
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        self._configs: Dict[str, Dict] = {}
        self._load_tool_configs()

    def _load_tool_configs(self):
        """Load all tool configurations from yaml files."""
        config_dir = Path(__file__).parent.parent / "config" / "tools"
        for config_file in config_dir.glob("*.yaml"):
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                self._configs[config['name']] = config

    def _create_langchain_tool(self, tool_instance: Any, config: Dict) -> BaseTool:
        """Create a LangChain Tool from our tool instance."""
        return Tool(
            name=config['name'],
            description=config['description'],
            func=tool_instance.run,
            coroutine=tool_instance.arun if hasattr(tool_instance, 'arun') else None,
            args_schema=tool_instance.args_schema if hasattr(tool_instance, 'args_schema') else None,
            return_direct=config.get('return_direct', False),
            handle_tool_error=True
        )

    def get_tool(self, tool_name: str, params: Dict[str, Any] = None) -> BaseTool:
        """Get a tool instance with specified parameters."""
        if tool_name not in self._tools:
            config = self._configs.get(tool_name)
            if not config:
                raise ValueError(f"No configuration found for tool: {tool_name}")

            if tool_name == "Summarizer":
                tool_instance = SummarizerTool()
                if params:
                    tool_instance.configure(params)
                self._tools[tool_name] = self._create_langchain_tool(tool_instance, config)
            else:
                raise ValueError(f"Unknown tool: {tool_name}")

        return self._tools[tool_name]

    def get_available_tools(self) -> List[BaseTool]:
        """Get list of all available tools."""
        return list(self._tools.values()) 