import os
from dotenv import load_dotenv
from src.workflows.workflow_executor import WorkflowExecutor
import argparse

def setup_environment():
    """Load environment variables and check for required API keys."""
    load_dotenv()
    
    required_keys = {
        'OPENAI_API_KEY': 'OpenAI',
        'GOOGLE_API_KEY': 'Gemini',
        'REPLICATE_API_TOKEN': 'Llama/Replicate'
    }
    
    missing_keys = []
    for env_key, service in required_keys.items():
        if env_key not in os.environ:
            missing_keys.append(f"{service} ({env_key})")
    
    if missing_keys:
        print("Warning: The following API keys are missing:")
        for key in missing_keys:
            print(f"- {key}")
        print("Some features may not work without these keys.\n")

def main():
    parser = argparse.ArgumentParser(description='AI Workflow Executor')
    parser.add_argument('--list', action='store_true', help='List available workflows')
    parser.add_argument('--workflow', type=str, help='Name of the workflow to execute')
    parser.add_argument('--input', type=str, help='Input text for the workflow')
    parser.add_argument('--input-file', type=str, help='Path to input file')
    
    args = parser.parse_args()
    
    # Setup environment
    setup_environment()
    
    # Initialize workflow executor
    executor = WorkflowExecutor()
    
    # List available workflows
    if args.list:
        print("\nAvailable workflows:")
        for workflow in executor.list_workflows():
            description = executor.get_workflow_description(workflow)
            print(f"\n- {workflow}")
            print(f"  Description: {description}")
        return

    # Execute workflow
    if args.workflow:
        # Get input from file or command line
        if args.input_file:
            try:
                with open(args.input_file, 'r') as f:
                    input_text = f.read()
            except Exception as e:
                print(f"Error reading input file: {str(e)}")
                return
        elif args.input:
            input_text = args.input
        else:
            print("Error: Please provide input text using --input or --input-file")
            return

        try:
            print(f"\nExecuting workflow: {args.workflow}")
            print("Input:", input_text[:100] + "..." if len(input_text) > 100 else input_text)
            print("\nProcessing...\n")
            
            result = executor.execute(args.workflow, input_text)
            
            print("\nResult:")
            print(result)
            
        except Exception as e:
            print(f"Error executing workflow: {str(e)}")
            return
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 