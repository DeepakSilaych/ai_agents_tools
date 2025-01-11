from setuptools import setup, find_packages

setup(
    name='ai-agents-tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langchain-core',
        'openai',
        'python-dotenv',
        'pydantic',
        'langchain-openai',
        'tavily-python',
        'duckduckgo-search'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'pytest-mock'
        ]
    }
) 