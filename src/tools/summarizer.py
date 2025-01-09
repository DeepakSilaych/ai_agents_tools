from typing import Dict, Any
from langchain.chains import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

class SummarizerTool:
    def __init__(self):
        self.max_length = 150
        self.chain_type = "stuff"

    def configure(self, params: Dict[str, Any]):
        """Configure tool parameters."""
        self.max_length = params.get('max_length', self.max_length)
        self.chain_type = params.get('chain_type', self.chain_type)

    def run(self, input_text: str, llm: Any) -> str:
        """Run the summarization tool."""
        prompt = ChatPromptTemplate.from_template(
            "Summarize the following text in {max_length} words or less:\n\n{context}"
        )
        
        # Create the chain
        chain = create_stuff_documents_chain(llm, prompt)
        
        # Create a document from input text
        doc = Document(page_content=input_text)
        
        # Run the chain
        result = chain.invoke({
            "context": [doc],
            "max_length": self.max_length
        })
        
        return result 