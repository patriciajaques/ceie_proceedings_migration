# src/adapters/ai_client_interface.py
from abc import ABC, abstractmethod


class AIClientInterface(ABC):
    """Abstract base class defining the interface for AI client implementations.

    This interface standardizes how AI completions are created across different
    AI service providers.
    """

    @abstractmethod
    def create_completion(self, user_message, is_json=False):
        """Creates a completion using the AI service.

        Args:
            user_message (str): The user's input message or query.
            is_json (bool, optional): Flag indicating if the response should be in JSON format.
                Defaults to False.

        Returns:
            str: The AI-generated completion response.

        Raises:
            NotImplementedError: This is an abstract method that must be implemented
                by concrete classes.
        """
        pass
