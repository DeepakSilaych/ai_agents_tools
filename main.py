import random
from workflows.web_search_workflow import create_workflow

def main():
    # List of potential web search scenarios
    scenarios = [
        {
            "context": "As an AI research assistant, I need to find the latest information",
            "query": "What are the most recent advancements in AI language models in 2023?"
        },
        {
            "context": "Researching current tech trends for a report",
            "query": "What are the top emerging technologies in artificial intelligence this year?"
        },
        {
            "context": "Gathering information for a technology overview",
            "query": "What are the key developments in generative AI in the past six months?"
        }
    ]

    # Randomly select a scenario
    selected_scenario = random.choice(scenarios)

    # Create web search workflow with the selected scenario
    workflow = create_workflow(
        input_text=f"{selected_scenario['context']}\n\n{selected_scenario['query']}"
    )

    # Run workflow
    result = workflow.run()

    # Print scenario and result
    print("Scenario Context:")
    print(selected_scenario['context'])
    print("\nOriginal Query:")
    print(selected_scenario['query'])
    print("\nWeb Search Result:")
    print(result)

if __name__ == "__main__":
    main()
