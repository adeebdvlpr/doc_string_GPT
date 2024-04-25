import logging
import vertexai
from vertexai.preview import reasoning_engines
from config import model, model_kwargs
from Capabilities.docstring_util import add_docstrings_to_js

def main():

    vertexai.init(
    project="docstringtool",
    location="us-central1",
    staging_bucket="gs://vertex_app_bucket ",
)
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    
        # Create LangChain agent
    agent = reasoning_engines.LangchainAgent(
            model=model,
            model_kwargs=model_kwargs,
        )

    try:
        # Test the application
        response = agent.query(
            input="what the most common pet name in the United States?"
        )
        logging.info("Response: %s", response)

    except Exception as e:
        logging.error("An error occurred: %s", e)
        raise
        

if __name__ == "__main__":
    main()

