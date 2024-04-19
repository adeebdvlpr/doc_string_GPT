import logging
from langchain_google_vertexai import reasoning_engines
from config import model, model_kwargs
from Capabilities.docstring_util import add_docstrings_to_js

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    try:
        # Create LangChain agent
        agent = reasoning_engines.LangchainAgent(
            model=model,
            tools=[add_docstrings_to_js],
            model_kwargs=model_kwargs,
        )

        # Test the application
        response = agent.query(
            input="Add docstrings to the JavaScript file 'example.js'."
        )
        logging.info("Response: %s", response)

    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise

if __name__ == "__main__":
    main()

