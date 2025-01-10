from typing import Union
from langchain_core.language_models import BaseChatModel
from .openai import get_openai_llm

def get_llm(llm_type: str) -> BaseChatModel:
    """
    Get LLM instance based on type
    
    Args:
        llm_type (str): Type of LLM to use (e.g. 'openai')
    
    Returns:
        BaseChatModel: Configured LLM instance
    """
    llm_map = {
        'openai': get_openai_llm
    }
    
    if llm_type not in llm_map:
        raise ValueError(f"Unsupported LLM type: {llm_type}")
        
    return llm_map[llm_type]()

def __init__(self, llm_type: str = 'openai'):
    return get_llm(llm_type)
