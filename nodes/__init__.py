from .text_to_markdown_tool import TextToMarkdownTool

AVAILABLE_TOOLS = [
    {
        'id': 'text_to_markdown',
        'tool': TextToMarkdownTool,
        'description': 'Converts plain text into markdown format'
    }
]

def get_tool_by_id(tool_id: str):
    """
    Retrieve a tool by its ID
    
    Args:
        tool_id (str): Tool identifier
    
    Returns:
        BaseTool: Instantiated tool
    """
    for tool_config in AVAILABLE_TOOLS:
        if tool_config['id'] == tool_id:
            return tool_config['tool']()
    return None




