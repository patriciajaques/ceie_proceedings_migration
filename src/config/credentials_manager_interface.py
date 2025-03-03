from abc import ABC, abstractmethod

class CredentialsManagerInterface(ABC):
    """
    Interface for managing credentials.

    This abstract base class defines the method that any credentials manager
    implementation must provide.

    Methods
    -------
    get_credentials()
        Abstract method to retrieve credentials. Must be implemented by subclasses.
    """
    @abstractmethod
    def get_credentials(self):
        pass


