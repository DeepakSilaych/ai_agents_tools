"""
Setup configuration for the project.
"""
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
        'duckduckgo-search',
        'openpyxl',
        'unstructured',
        'python-docx',
        'python-pptx',
        'beautifulsoup4',
        'markdown',
        'pypdf',
        'lxml'
    ]
) 