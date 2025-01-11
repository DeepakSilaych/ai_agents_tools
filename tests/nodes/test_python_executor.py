"""
Manual test script for Python Executor Tool.
"""
import os
from nodes.python_executor import PythonExecutorTool

def test_python_executor():
    """
    Manually test the Python Executor Tool with various code snippets.
    """
    e2b_api_key = os.getenv('E2B_API_KEY')
    if not e2b_api_key:
        print("Warning: E2B_API_KEY not set. Please set it in .env file.")
        return

    python_tool = PythonExecutorTool(api_key=e2b_api_key)

    test_cases = [
        {
            'name': 'Simple Arithmetic',
            'code': 'print(2 + 3 * 4)'
        },
        {
            'name': 'For Loop',
            'code': 'for i in range(5): print(i)'
        },
        {
            'name': 'Error Handling',
            'code': 'print(undefined_variable)'
        },
        {
            'name': 'Data Processing',
            'code': '''
import pandas as pd
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print(df.sum())
'''
        }
    ]

    for case in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing: {case['name']}")
        print(f"{'='*50}")
        print("Code:")
        print(case['code'])
        print("\nOutput:")
        result = python_tool._run(case['code'])
        print(result)

if __name__ == "__main__":
    test_python_executor() 