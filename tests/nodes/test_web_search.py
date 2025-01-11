"""
Test suite for the WebSearchTool.
"""

from nodes.web_search import WebSearchTool


if __name__ == "__main__":
    print("Running manual test for WebSearch")
    tool = WebSearchTool()
    query = "AI advancements in 2023"
    result = tool._run(query)
    print(result)