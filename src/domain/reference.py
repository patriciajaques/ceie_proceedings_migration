# src/domain/reference.py
from typing import Dict, Any, Optional
from src.domain.base_model import BaseModel


class Reference(BaseModel):
    """
    Represents a bibliographic reference in an academic article.

    This class encapsulates all data related to a reference,
    including its description, identifiers, and links.
    """

    # Define the mapping from dictionary keys to object attributes
    field_mapping = {
        "description": "description",
        "doi": "doi",
        "link": "link",
        "accessed": "accessed",
        "order": "order",
    }

    # Define the reverse mapping from object attributes to dictionary keys
    reverse_field_mapping = {
        "description": "description",
        "doi": "doi",
        "link": "link",
        "accessed": "accessed",
        "order": "order",
    }

    def __init__(
        self,
        description: str = "",
        doi: str = "",
        link: str = "",
        accessed: str = "",
        order: int = 0,
        **kwargs
    ):
        """
        Initialize a Reference object.

        Args:
            description: Bibliographic description
            doi: Digital Object Identifier
            link: URL to the referenced resource
            accessed: Date when the resource was last accessed
            order: Reference order in the article
            **kwargs: Additional attributes
        """
        self.description = description
        self.doi = doi
        self.link = link
        self.accessed = accessed
        self.order = order

        # Handle additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        """
        String representation of the Reference.

        Returns:
            str: Reference description
        """
        return self.description
