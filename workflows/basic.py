from typing import List, Any, Optional
from langchain_core.tools import BaseTool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

from llm import get_llm
from nodes import AVAILABLE_TOOLS 

class GenericWorkflow:
    def __init__(
        self, 
        input_text: str, 
        llm: str
    ):
        """
        Initialize a generic workflow
        
        Args:
            input_text (str): Input text to process
            tools (List[BaseTool], optional): List of tools to potentially use
            use_markdown (bool, optional): Whether to convert output to markdown
        """

        self.llm = get_llm(llm)
        
        self.input_text = input_text

        tools_description = "\n".join([
            f"- {tool_config['id']}: {tool_config['description']}" 
            for tool_config in AVAILABLE_TOOLS
        ])
        
        self.prompt = ChatPromptTemplate.from_template(
            "You are an AI assistant helping an intern at an AI firm process research data.\n\n"
            f"Available tools:\n{tools_description}\n\n"
            "Context: You are helping process and structure research data. Some tools are available for post-processing.\n\n"
            "Guidelines:\n"
            "1. Carefully analyze the input text\n"
            "2. Provide a comprehensive and structured response\n"
            "3. If a tool can help improve the output, explicitly mention the tool's name\n"
            "4. Focus on clarity, coherence, and research-oriented formatting\n\n"
            "Input text:\n{text}"
        )
    
    def run(self) -> str:
        """
        Execute the workflow
        
        Returns:
            str: Processed output
        """
        workflow = (
            RunnablePassthrough.assign(
                llm_output=self.prompt | self.llm
            )
        )
        
        result = workflow.invoke({
            "text": self.input_text
        })
        
        output = result['llm_output'].content
        
        for tool_config in AVAILABLE_TOOLS:
            tool_name = tool_config['id']
            if tool_name in output.lower():
                try:
                    tool = tool_config['tool']()
                    output = tool.run(output)
                except Exception as e:
                    print(f"Tool {tool_name} failed: {e}")
        return output

def create_workflow(
    input_text: str, 
    llm: str = 'openai',
):
    """
    Create and return a workflow instance
    
    Args:
        input_text (str): Input text to process
        tools (List[BaseTool], optional): List of tools to potentially use
        use_markdown (bool, optional): Whether to convert output to markdown
    
    Returns:
        GenericWorkflow: Workflow instance
    """
    return GenericWorkflow(input_text, llm)