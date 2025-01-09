import os
from ..core.workflow_orchestrator import WorkflowOrchestrator

def test_basic_summary_workflow():
    # Ensure OPENAI_API_KEY is set
    assert "OPENAI_API_KEY" in os.environ, "OPENAI_API_KEY must be set"
    
    orchestrator = WorkflowOrchestrator()
    
    test_input = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals including humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals.
    """
    
    result = orchestrator.execute_workflow("Basic Summary Workflow", test_input)
    
    assert result, "Result should not be empty"
    print(f"Summary result: {result}")

if __name__ == "__main__":
    test_basic_summary_workflow() 