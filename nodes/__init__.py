"""
Initialize and manage available tools for the workflow.
"""
from .text_to_markdown_tool import TextToMarkdownTool
from .web_search import WebSearchTool

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
    }
]

def get_tool_by_id(tool_id: str):
    for tool_config in AVAILABLE_TOOLS:
        if tool_config['id'] == tool_id:
            return tool_config['tool']()
    return None




