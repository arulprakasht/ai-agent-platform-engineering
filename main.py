import os

def main():
    # Initialize and start the AI agent for platform engineering tasks
    print("Starting AI Agent for Platform Engineering...")

    # Load environment variables
    load_env_variables()

    # Add your AI agent logic here

def load_env_variables():
    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()

    # Print loaded environment variables for debugging purposes
    for key, value in os.environ.items():
        print(f"{key}={value}")

if __name__ == "__main__":
    main()