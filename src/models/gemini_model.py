from typing import Any, Dict, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .base_model import BaseModel

class GeminiModel(BaseModel):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        self.model = ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=self.temperature,
            streaming=self.streaming,
            callback_manager=self.callback_manager
        )

    def generate(self, prompt: str) -> str:
        """Generate response using Gemini model."""
        return self.model.invoke(prompt).content

    def chat(self, messages: list) -> str:
        """Chat using Gemini model."""
        return self.model.invoke(messages).content 