"""
Manual test script for File Loader Tool.
"""
import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

from nodes.file_loader_tool import FileLoaderTool

def test_file_loader():
    """
    Manually test the File Loader Tool with sample files.
    """
    tool = FileLoaderTool()

    # Create example_data directory if it doesn't exist
    data_dir = Path(project_root) / "example_data"
    data_dir.mkdir(exist_ok=True)

    # Create sample files for testing
    create_sample_files(data_dir)

    # Test cases for different file formats
    test_cases = [
        {
            'name': 'CSV File',
            'file': str(data_dir / 'sample.csv'),
            'source_column': 'name'
        },
        {
            'name': 'Text File',
            'file': str(data_dir / 'sample.txt')
        },
        {
            'name': 'JSON File',
            'file': str(data_dir / 'sample.json')
        }
    ]

    # Run tests
    for case in test_cases:
        print(f"\n{'='*50}")
        print(f"Testing: {case['name']}")
        print(f"{'='*50}")
        print(f"File: {case['file']}")
        
        if os.path.exists(case['file']):
            try:
                result = tool._run(
                    file_path=case['file'],
                    source_column=case.get('source_column')
                )
                print("\nResult:")
                print(result)
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print(f"File not found: {case['file']}")

def create_sample_files(data_dir: Path):
    """Create sample files for testing."""
    # Create CSV file
    with open(data_dir / 'sample.csv', 'w') as f:
        f.write("name,age,city\nJohn,30,New York\nJane,25,London")

    # Create text file
    with open(data_dir / 'sample.txt', 'w') as f:
        f.write("This is a sample text file.\nIt has multiple lines.\nUsed for testing.")

    # Create JSON file
    with open(data_dir / 'sample.json', 'w') as f:
        f.write('{"data": {"name": "John", "age": 30, "city": "New York"}}')

if __name__ == "__main__":
    test_file_loader() 