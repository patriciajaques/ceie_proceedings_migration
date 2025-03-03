from src.config.credentials_manager_interface import CredentialsManagerInterface
import os
from dotenv import load_dotenv


class OpenAICredentialsManager(CredentialsManagerInterface):
    """
    Class to manage OpenAI credentials from environment variables.
    """

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

    def get_credentials(self):
        """
        Get OpenAI credentials from environment variables.

        Returns:
            dict: Dictionary containing the API key.
        """
        return {"api_key": os.environ.get("OPENAI_API_KEY")}
