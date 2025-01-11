"""
Test runner script for the project.
"""
import os
import sys
import pytest

def run_tests():
    """
    Run project tests with coverage.
    """
    # Add project root to Python path
    project_root = os.path.abspath(os.path.dirname(__file__))
    sys.path.insert(0, project_root)

    # Arguments for pytest
    pytest_args = [
        '-v',  # verbose output
        '--cov=nodes',  # coverage for nodes directory
        '--cov-report=term-missing',  # show lines not covered
        'tests/'  # test directory
    ]
    
    # Run tests
    result = pytest.main(pytest_args)
    
    # Exit with pytest's return code
    sys.exit(result)

if __name__ == '__main__':
    run_tests() 