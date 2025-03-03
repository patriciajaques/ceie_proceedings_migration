# src/adapters/anthropic_client.py
from anthropic import Anthropic
from src.adapters.base_ai_client import BaseAIClient
from src.config.config_loader import ConfigLoader
from src.config.anthropic_credentials_manager import AnthropicCredentialsManager
from src.config.credentials_manager_interface import CredentialsManagerInterface


class AnthropicClient(BaseAIClient):
    """
    Client for the Anthropic API service.

    Implements the BaseAIClient interface to communicate
    with Anthropic Claude services for text generation.
    """

    def __init__(self, config_loader: ConfigLoader, prompt_key: str):
        """
        Initialize the Anthropic client.

        Args:
            config_loader (ConfigLoader): Configuration loader instance.
            prompt_key (str): Key for the prompt to be loaded.
        """
        self.model = config_loader.get_config_value(
            "anthropic_model", "claude-3-opus-20240229"
        )
        super().__init__(config_loader, prompt_key)

    def get_credentials_manager(self) -> CredentialsManagerInterface:
        """
        Return the Anthropic credentials manager.

        Returns:
            CredentialsManagerInterface: The credentials manager.
        """
        return AnthropicCredentialsManager()

    def initialize_client(self):
        """
        Initialize the Anthropic API client.

        Returns:
            Anthropic: Initialized Anthropic API client.
        """
        return Anthropic(api_key=self.api_key)

    def create_completion(self, user_message, is_json=False):
        """
        Create a completion using the Anthropic API.

        Args:
            user_message (str): User message.
            is_json (bool, optional): If True, requests response in JSON format.
                Defaults to False.

        Returns:
            str: Anthropic API response.
        """
        try:
            response = self.client.messages.create(
                model=self.model,
                system=self.system_message,
                messages=[{"role": "user", "content": user_message}],
                temperature=0,
                max_tokens=4000,
            )
            return response.content[0].text
        except Exception as e:
            print(f"\n\nError creating Anthropic completion: {e}")
            return ""
