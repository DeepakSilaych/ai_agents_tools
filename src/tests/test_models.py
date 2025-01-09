import os
from dotenv import load_dotenv
from ..core.model_manager import ModelManager

def test_models():
    # Load environment variables
    load_dotenv()
    
    # Ensure required API keys are set
    required_keys = {
        'OPENAI_API_KEY': 'OpenAI',
        'GOOGLE_API_KEY': 'Gemini',
        'REPLICATE_API_TOKEN': 'Llama/Replicate'
    }
    
    for env_key, service in required_keys.items():
        if env_key not in os.environ:
            print(f"Warning: {env_key} not set. {service} models will not work.")
    
    model_manager = ModelManager()
    
    # Test prompt
    test_prompt = "Explain what is artificial intelligence in one sentence."
    
    # Test different models
    models_to_test = ['gpt-3.5-turbo', 'gemini-pro', 'llama-2-70b-chat']
    
    for model_name in models_to_test:
        try:
            print(f"\nTesting {model_name}...")
            model = model_manager.get_model(model_name)
            response = model.generate(test_prompt)
            print(f"Response: {response}")
        except Exception as e:
            print(f"Error testing {model_name}: {str(e)}")

if __name__ == "__main__":
    test_models() 