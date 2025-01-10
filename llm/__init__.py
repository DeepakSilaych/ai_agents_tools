from typing import Union
from langchain_core.language_models import BaseChatModel
from .openai import get_openai_llm
from .gemini import get_gemini_llm

def get_llm(llm_type="openai"):
    if llm_type == "openai":
        return get_openai_llm()
    elif llm_type == "gemini":
        return get_gemini_llm()
    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")

def __init__(self, llm_type: str = 'openai'):
    return get_llm(llm_type)
