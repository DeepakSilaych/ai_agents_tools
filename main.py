import random
from workflows.basic import create_workflow

def main():
    # List of potential scenarios to generate a query that might need tool processing
    scenarios = [
        {
            "context": "As an AI intern at a data analytics firm, I'm working on a project about tech industry trends.",
            "query": "I've collected raw interview notes from tech professionals about AI's impact. Can you help me organize and structure these notes for our research report? The notes are quite unstructured and need careful formatting."
        },
        {
            "context": "I'm an intern at a machine learning startup, helping to curate training datasets.",
            "query": "We've gathered a large collection of unformatted text snippets from various sources. I need to prepare these for our NLP model training. The text needs careful preprocessing and standardization."
        },
        {
            "context": "Working as an AI research intern at a knowledge management firm.",
            "query": "I've collected interview transcripts about emerging technologies. Our team needs these converted into a clean, readable format for our quarterly report. The current notes are quite messy."
        }
    ]

    # Randomly select a scenario
    selected_scenario = random.choice(scenarios)

    # Create workflow with the selected scenario
    workflow = create_workflow(
        input_text=f"{selected_scenario['context']}\n\n{selected_scenario['query']}",
        llm='gemini'
    )

    # Run workflow
    result = workflow.run()

    # Print scenario and result
    print("Scenario Context:")
    print(selected_scenario['context'])
    print("\nOriginal Query:")
    print(selected_scenario['query'])
    print("\nWorkflow Result:")
    print(result)

if __name__ == "__main__":
    main()
