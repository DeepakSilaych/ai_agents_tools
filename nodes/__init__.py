"""
Initialize and manage available tools for the workflow.
"""
from .text_to_markdown_tool import TextToMarkdownTool
from .web_search import WebSearchTool
from .python_executor import PythonExecutorTool
from .file_loader_tool import FileLoaderTool

AVAILABLE_TOOLS = [
    {
        'id': 'text_to_markdown',
        'tool': TextToMarkdownTool,
        'description': 'Converts plain text into markdown format'
    },
    {
        'id': 'web_search',
        'tool': WebSearchTool,
        'description': 'Search the web for information'
    },
    {
        'id': 'python_executor',
        'tool': PythonExecutorTool,
        'description': 'Execute Python code in a sandboxed environment'
    },
    {
        'id': 'file_loader',
        'tool': FileLoaderTool,
        'description': 'Load and process CSV and Excel files'
    }
]

def get_tool_by_id(tool_id: str):
    for tool_config in AVAILABLE_TOOLS:
        if tool_config['id'] == tool_id:
            return tool_config['tool']()
    return None




