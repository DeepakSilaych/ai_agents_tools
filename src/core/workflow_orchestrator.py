import yaml
from pathlib import Path
from typing import Dict, Any, List
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from .tool_manager import ToolManager
from .model_manager import ModelManager

class WorkflowOrchestrator:
    def __init__(self):
        self.tool_manager = ToolManager()
        self.model_manager = ModelManager()
        self._workflows = {}
        self._agents = {}
        self._load_workflows()

    def _load_workflows(self):
        """Load all workflow configurations."""
        workflow_dir = Path(__file__).parent.parent / "config" / "workflows"
        for workflow_file in workflow_dir.glob("*.yaml"):
            with open(workflow_file, 'r') as f:
                workflow = yaml.safe_load(f)
                self._workflows[workflow['name']] = workflow

    def _create_agent(self, workflow: Dict[str, Any], llm: Any):
        """Create a LangChain agent for the workflow."""
        tools = []
        for tool_config in workflow['tools']:
            tool = self.tool_manager.get_tool(
                tool_config['name'],
                tool_config.get('params', {})
            )
            tools.append(tool)

        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Initialize agent with tools and memory
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=memory,
            verbose=True,
            system_message=SystemMessage(content=workflow.get('system_message', ''))
        )

        return agent

    def execute_workflow(self, workflow_name: str, input_data: str) -> str:
        """Execute a workflow by name with given input data."""
        if workflow_name not in self._workflows:
            raise ValueError(f"Unknown workflow: {workflow_name}")

        workflow = self._workflows[workflow_name]
        
        # Get or create agent for this workflow
        if workflow_name not in self._agents:
            llm = self.model_manager.get_model(workflow.get('model'))
            self._agents[workflow_name] = self._create_agent(workflow, llm)

        agent = self._agents[workflow_name]
        
        # Execute the workflow using the agent
        result = agent.run(input=input_data)
        return result 