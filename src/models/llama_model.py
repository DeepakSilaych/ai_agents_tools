from typing import Any, Dict, Optional
from langchain_community.llms import Replicate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from .base_model import BaseModel

class LlamaModel(BaseModel):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        # Llama-2 model ID on Replicate
        self.llama_id = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
        
        self.model = Replicate(
            model=self.llama_id,
            temperature=self.temperature,
            callback_manager=self.callback_manager
        )

    def generate(self, prompt: str) -> str:
        """Generate response using Llama model."""
        return self.model.invoke(prompt)

    def chat(self, messages: list) -> str:
        """Chat using Llama model."""
        formatted_prompt = self._format_chat_messages(messages)
        return self.model.invoke(formatted_prompt)

    def _format_chat_messages(self, messages: list) -> str:
        """Format chat messages for Llama model."""
        formatted = []
        for msg in messages:
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            if role == 'system':
                formatted.append(f"<system>{content}</system>")
            elif role == 'assistant':
                formatted.append(f"<assistant>{content}</assistant>")
            else:
                formatted.append(f"<user>{content}</user>")
        return "\n".join(formatted) 