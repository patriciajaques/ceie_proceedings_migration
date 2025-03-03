# src/domain/author.py
from typing import Dict, Any, Optional
from src.domain.base_model import BaseModel


class Author(BaseModel):
    """
    Represents an author of an academic article.

    This class encapsulates all data related to an article author,
    including personal information and institutional affiliation.
    """

    # Define the mapping from dictionary keys to object attributes
    field_mapping = {
        "authorFirstName": "first_name",
        "authorMiddleName": "middle_name",
        "authorLastName": "last_name",
        "authorAffiliation": "affiliation",
        "authorAffiliationEn": "affiliation_en",
        "authorCountry": "country",
        "authorEmail": "email",
        "orcid": "orcid",
        "order": "order",
    }

    # Define the reverse mapping from object attributes to dictionary keys
    reverse_field_mapping = {
        "first_name": "authorFirstName",
        "middle_name": "authorMiddleName",
        "last_name": "authorLastName",
        "affiliation": "authorAffiliation",
        "affiliation_en": "authorAffiliationEn",
        "country": "authorCountry",
        "email": "authorEmail",
        "orcid": "orcid",
        "order": "order",
    }

    def __init__(
        self,
        first_name: str = "",
        middle_name: str = "",
        last_name: str = "",
        affiliation: str = "",
        affiliation_en: str = "",
        country: str = "",
        email: str = "",
        orcid: str = "",
        order: int = 0,
        **kwargs,
    ):
        """
        Initialize an Author object.

        Args:
            first_name: Author's first name
            middle_name: Author's middle name(s)
            last_name: Author's last name
            affiliation: Institutional affiliation in original language
            affiliation_en: Institutional affiliation in English
            country: Country of affiliation
            email: Contact email
            orcid: ORCID identifier
            order: Author order in the article
            **kwargs: Additional attributes
        """
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.affiliation = affiliation
        self.affiliation_en = affiliation_en
        self.country = country
        self.email = email
        self.orcid = orcid
        self.order = order

        # Handle additional attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def full_name(self) -> str:
        """
        Get the author's full name.

        Returns:
            str: Full name with all components
        """
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        """
        String representation of the Author.

        Returns:
            str: Author's full name
        """
        return self.full_name
