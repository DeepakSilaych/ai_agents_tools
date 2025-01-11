"""
Global pytest configuration to add project root to Python path.
"""
import os
import sys

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))) 