"""
Tool for loading and processing various file formats using local libraries.
"""
from typing import Optional, Type, List
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from langchain_community.document_loaders import (
    CSVLoader,
    UnstructuredExcelLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    JSONLoader,
    BSHTMLLoader,
    UnstructuredXMLLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader
)
import json
from pathlib import Path

class FileLoaderInput(BaseModel):
    file_path: str = Field(description="Path to the file to load")
    source_column: Optional[str] = Field(description="Column to use as source for CSV files", default=None)
    encoding: Optional[str] = Field(description="File encoding", default="utf-8")
    jq_schema: Optional[str] = Field(description="JQ schema for JSON files", default=None)

class FileLoaderTool(BaseTool):
    name: str = "file_loader"
    description: str = "Load and process files of various formats (CSV, Excel, PDF, Text, Markdown, JSON, HTML, XML, PPT, DOC)"
    args_schema: Type[BaseModel] = FileLoaderInput

    def _run(
        self, 
        file_path: str, 
        source_column: Optional[str] = None,
        encoding: Optional[str] = "utf-8",
        jq_schema: Optional[str] = None
    ) -> str:
        try:
            file_extension = Path(file_path).suffix.lower()
            
            loaders = {
                '.csv': self._load_csv,
                '.xlsx': self._load_excel,
                '.xls': self._load_excel,
                '.pdf': self._load_pdf,
                '.txt': self._load_text,
                '.md': self._load_markdown,
                '.json': self._load_json,
                '.html': self._load_html,
                '.htm': self._load_html,
                '.xml': self._load_xml,
                '.pptx': self._load_powerpoint,
                '.ppt': self._load_powerpoint,
                '.docx': self._load_word,
                '.doc': self._load_word
            }
            
            if file_extension not in loaders:
                return f"Unsupported file format: {file_extension}"
            
            loader_func = loaders[file_extension]
            documents = loader_func(
                file_path=file_path,
                source_column=source_column,
                encoding=encoding,
                jq_schema=jq_schema
            )
            
            return self._format_documents(documents)
            
        except Exception as e:
            return f"Error loading file: {str(e)}"

    def _load_csv(self, file_path: str, source_column: Optional[str] = None, **kwargs) -> List:
        loader = CSVLoader(
            file_path=file_path,
            source_column=source_column,
            csv_args={
                'delimiter': ',',
                'quotechar': '"',
                'encoding': kwargs.get('encoding', 'utf-8')
            }
        )
        return loader.load()

    def _load_excel(self, file_path: str, **kwargs) -> List:
        loader = UnstructuredExcelLoader(
            file_path=file_path,
            mode="elements"
        )
        return loader.load()

    def _load_pdf(self, file_path: str, **kwargs) -> List:
        loader = PyPDFLoader(file_path)
        return loader.load()

    def _load_text(self, file_path: str, **kwargs) -> List:
        loader = TextLoader(
            file_path,
            encoding=kwargs.get('encoding', 'utf-8')
        )
        return loader.load()

    def _load_markdown(self, file_path: str, **kwargs) -> List:
        loader = UnstructuredMarkdownLoader(
            file_path,
            mode="elements"
        )
        return loader.load()

    def _load_json(self, file_path: str, **kwargs) -> List:
        jq_schema = kwargs.get('jq_schema', '.')
        loader = JSONLoader(
            file_path=file_path,
            jq_schema=jq_schema,
            text_content=False
        )
        return loader.load()

    def _load_html(self, file_path: str, **kwargs) -> List:
        loader = BSHTMLLoader(
            file_path,
            open_encoding=kwargs.get('encoding', 'utf-8')
        )
        return loader.load()

    def _load_xml(self, file_path: str, **kwargs) -> List:
        loader = UnstructuredXMLLoader(
            file_path,
            mode="elements"
        )
        return loader.load()

    def _load_powerpoint(self, file_path: str, **kwargs) -> List:
        loader = UnstructuredPowerPointLoader(
            file_path,
            mode="elements"
        )
        return loader.load()

    def _load_word(self, file_path: str, **kwargs) -> List:
        loader = UnstructuredWordDocumentLoader(
            file_path,
            mode="elements"
        )
        return loader.load()

    def _format_documents(self, documents: list) -> str:
        formatted_output = []
        for doc in documents:
            content = doc.page_content.strip()
            metadata = doc.metadata
            formatted_output.append(
                f"Content:\n{content}\n\nMetadata:\n{metadata}\n{'='*50}"
            )
        return "\n".join(formatted_output) 