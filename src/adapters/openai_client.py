# src/adapters/openai_client.py
from openai import OpenAI
from src.adapters.base_ai_client import BaseAIClient
from src.config.config_loader import ConfigLoader
from src.config.openai_credentials_manager import OpenAICredentialsManager
from src.config.credentials_manager_interface import CredentialsManagerInterface


class OpenAIClient(BaseAIClient):
    """
    Client for the OpenAI API service.

    Implements the BaseAIClient interface to communicate
    with OpenAI services for text generation.
    """

    def __init__(self, config_loader: ConfigLoader, prompt_key: str):
        """
        Initialize the OpenAI client.

        Args:
            config_loader (ConfigLoader): Configuration loader instance.
            prompt_key (str): Key for the prompt to be loaded.
        """
        self.model = config_loader.get_config_value("engine")
        super().__init__(config_loader, prompt_key)

    def get_credentials_manager(self) -> CredentialsManagerInterface:
        """
        Return the OpenAI credentials manager.

        Returns:
            CredentialsManagerInterface: The credentials manager.
        """
        return OpenAICredentialsManager()

    def initialize_client(self):
        """
        Initialize the OpenAI API client.

        Returns:
            OpenAI: Initialized OpenAI API client.
        """
        return OpenAI(api_key=self.api_key)

    def create_completion(self, user_message, is_json=False):
        """
        Create a completion using the OpenAI API.

        Args:
            user_message (str): User message.
            is_json (bool, optional): If True, requests response in JSON format.
                Defaults to False.

        Returns:
            str: OpenAI API response.
        """
        try:
            return_type = "json_object" if is_json else "text"
            completion = self.client.chat.completions.create(
                model=self.model,
                response_format={"type": return_type},
                messages=[
                    {"role": "system", "content": self.system_message},
                    {"role": "user", "content": user_message},
                ],
                temperature=0,
                max_tokens=4000,
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"\n\nError creating OpenAI completion: {e}")
            return ""
