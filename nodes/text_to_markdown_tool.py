"""
Tool for converting plain text to markdown format.
"""
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class TextToMarkdownInput(BaseModel):
    text: str = Field(description="The text to convert to markdown")

class TextToMarkdownTool(BaseTool):
    name: str = "text_to_markdown"
    description: str = "Converts plain text into markdown format"
    args_schema: Type[BaseModel] = TextToMarkdownInput

    def _run(self, text: str) -> str:
        try:
            markdown_text = self._convert_to_markdown(text)
            return markdown_text
        except Exception as e:
            return f"Error converting text to markdown: {str(e)}"

    def _convert_to_markdown(self, text: str) -> str:
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