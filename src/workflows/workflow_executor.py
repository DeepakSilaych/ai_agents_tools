from typing import Dict, Any
from ..core.workflow_orchestrator import WorkflowOrchestrator
from pathlib import Path
import yaml

class WorkflowExecutor:
    def __init__(self):
        self.orchestrator = WorkflowOrchestrator()
        self._available_workflows = self._load_available_workflows()

    def _load_available_workflows(self) -> Dict[str, Dict[str, Any]]:
        """Load all available workflow configurations."""
        workflows = {}
        workflow_dir = Path(__file__).parent.parent / "config" / "workflows"
        for workflow_file in workflow_dir.glob("*.yaml"):
            with open(workflow_file, 'r') as f:
                workflow = yaml.safe_load(f)
                workflows[workflow['name']] = workflow
        return workflows

    def list_workflows(self) -> list:
        """Return list of available workflow names."""
        return list(self._available_workflows.keys())

    def get_workflow_description(self, workflow_name: str) -> str:
        """Get description of a specific workflow."""
        workflow = self._available_workflows.get(workflow_name)
        if not workflow:
            raise ValueError(f"Workflow not found: {workflow_name}")
        return workflow.get('description', 'No description available')

    def execute(self, workflow_name: str, input_data: str) -> str:
        """Execute a specific workflow."""
        return self.orchestrator.execute_workflow(workflow_name, input_data) 