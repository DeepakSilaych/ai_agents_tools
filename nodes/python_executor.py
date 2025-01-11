"""
Tool for executing Python code in a sandboxed environment.
"""
import os
from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
import e2b

class PythonCodeInput(BaseModel):
    code: str = Field(description="Python code to execute")

class PythonExecutorTool(BaseTool):
    name: str = "python_executor"
    description: str = "Execute Python code in a sandboxed environment"
    args_schema: Type[BaseModel] = PythonCodeInput

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Python executor tool.
        
        Args:
            api_key (Optional[str]): E2B API key. If not provided, 
                                     tries to read from environment variable.
        """
        super().__init__()
        
        # Get API key from parameter or environment
        e2b_api_key = api_key or os.getenv('E2B_API_KEY')
        
        if not e2b_api_key:
            raise ValueError("E2B API key is required. Set E2B_API_KEY environment variable.")
        
        # Set the API key for E2B
        os.environ['E2B_API_KEY'] = e2b_api_key

    def _run(self, code: str) -> str:
        """
        Execute Python code in a sandboxed environment.
        
        Args:
            code (str): Python code to execute
        
        Returns:
            str: Output of the executed code
        """
        try:
            # Create a new E2B data analysis sandbox
            sandbox = e2b.DataAnalysisTool()
            
            # Execute the code
            result = sandbox.run_python(code)
            
            # Close the sandbox
            sandbox.close()
            
            return result
        except Exception as e:
            return f"Error executing Python code: {str(e)}"

    def as_tool(self):
        """
        Convert the tool to a Langchain tool format.
        
        Returns:
            dict: Tool configuration
        """
        return {
            "name": self.name,
            "description": self.description,
            "func": self._run
        } 