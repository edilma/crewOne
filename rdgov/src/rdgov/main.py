import sys
import warnings
from datetime import datetime
from rdgov.crew import Rdgov

warnings.filterwarnings("ignore")

def run():
    """
    Run the crew execution.
    """
    inputs = {
        'task': 'Write a blog post about Nvidia stock performance',
        'current_date': '2024-04-23'
    }

    try:
        result = Rdgov().crew().kickoff(inputs=inputs)
        print("Execution Result:")
        print(result)
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <run|train|replay|test>")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "run":
        run()
    else:
        print("Invalid command. Available commands: run")
