from typing import Optional, Dict, Any
from ..models.openai_model import OpenAIModel
from ..models.gemini_model import GeminiModel
from ..models.llama_model import LlamaModel
import yaml
from pathlib import Path

class ModelManager:
    def __init__(self):
        self._models: Dict[str, Any] = {}
        self._default_model = None
        self._load_model_configs()

    def _load_model_configs(self):
        """Load model configurations from yaml file."""
        config_path = Path(__file__).parent.parent / "config" / "models.yaml"
        with open(config_path, 'r') as f:
            self._model_configs = yaml.safe_load(f)['models']

    def load_model(self, model_config: Dict[str, Any]):
        """Load and cache a model instance based on configuration."""
        model_name = model_config['name']
        
        if model_name not in self._models:
            provider = model_config['provider'].lower()
            
            if provider == 'openai':
                model = OpenAIModel(model_config)
            elif provider == 'google':
                model = GeminiModel(model_config)
            elif provider == 'replicate':
                model = LlamaModel(model_config)
            else:
                raise ValueError(f"Unsupported model provider: {provider}")
            
            self._models[model_name] = model
            if model_config.get('default', False):
                self._default_model = model

        return self._models[model_name]

    def get_model(self, model_name: Optional[str] = None) -> Any:
        """Get a model instance by name or return default."""
        if model_name:
            config = next((m for m in self._model_configs if m['name'] == model_name), None)
            if config:
                return self.load_model(config)
            raise ValueError(f"Model configuration not found: {model_name}")
            
        if not self._default_model:
            # Load default OpenAI model if none specified
            default_config = next(m for m in self._model_configs if m.get('default', False))
            return self.load_model(default_config)
            
        return self._default_model 