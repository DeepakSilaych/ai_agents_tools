from langchain_core.tools import BaseTool
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Type

class TextToMarkdownInput(BaseModel):
    """Input model for text to markdown conversion."""
    text: str = Field(description="The text to convert to markdown")

class TextToMarkdownTool(BaseTool):
    """Tool to convert plain text to markdown."""

    name: str = "text_to_markdown"
    description: str = "Converts plain text into markdown format"
    args_schema: Type[BaseModel] = TextToMarkdownInput

    def _run(self, text: str) -> str:
        """
        Convert text to markdown.
        
        Args:
            text (str): Input text to convert
        
        Returns:
            str: Markdown formatted text
        """
        try:
            markdown_text = self._convert_to_markdown(text)
            return markdown_text
        except Exception as e:
            return f"Error converting text to markdown: {str(e)}"

    def _convert_to_markdown(self, text: str) -> str:
        """
        Implement basic markdown conversion logic.
        
        Args:
            text (str): Input text
        
        Returns:
            str: Markdown formatted text
        """
        paragraphs = text.split('\n\n')
        
        markdown_paragraphs = []
        for para in paragraphs:
            if para.startswith('#'):
                markdown_paragraphs.append(para)
            elif para.startswith('- ') or para.startswith('* '):
                markdown_paragraphs.append(para)
            else:
                markdown_paragraphs.append(para)
        
        return '\n\n'.join(markdown_paragraphs) 