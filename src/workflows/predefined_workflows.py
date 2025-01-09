from typing import Dict, Any

class PredefinedWorkflows:
    """Collection of predefined workflow configurations."""
    
    @staticmethod
    def get_summary_workflow() -> Dict[str, Any]:
        return {
            "name": "Basic Summary Workflow",
            "description": "A simple workflow that summarizes text",
            "tools": [
                {
                    "name": "Summarizer",
                    "params": {
                        "max_length": 200,
                        "chain_type": "stuff"
                    }
                }
            ]
        }

    @staticmethod
    def get_all_workflows() -> Dict[str, Dict[str, Any]]:
        return {
            "Basic Summary Workflow": PredefinedWorkflows.get_summary_workflow()
        } 