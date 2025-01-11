"""
Test suite for the TextToMarkdownTool.
"""

from nodes.text_to_markdown_tool import TextToMarkdownTool

if __name__ == "__main__":
    print("Running manual test for TextToMarkdown")
    tool = TextToMarkdownTool()
    input_text = "<h1>Convert this text to markdown</h1>"
    result = tool._run(input_text)
    print(result+ "\n" + "___________________")