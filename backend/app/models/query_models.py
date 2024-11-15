from pydantic import BaseModel, Field, validator
from typing import List, Optional
from enum import Enum

class SearchType(str, Enum):
    """Enum for different types of search operations"""
    EMAIL = "email"
    CONTACT = "contact"
    ADDRESS = "address"
    WEBSITE = "website"
    GENERIC = "generic"

class SearchQueryModel(BaseModel):
    """
    Represents a search query with various validation rules
    """
    column: str = Field(..., min_length=1, description="Column to search in")
    prompt: str = Field(..., min_length=5, max_length=500,
                        description="Search prompt for information extraction")
    search_type: SearchType = Field(
        default=SearchType.GENERIC,
        description="Type of search to perform"
    )
    limit: Optional[int] = Field(
        default=10,
        ge=1,
        le=50,
        description="Maximum number of results to return"
    )

    @validator('prompt')
    def validate_prompt(cls, prompt):
        """
        Custom validation for prompt
        Ensures prompt contains meaningful search criteria
        """
        forbidden_words = ['hack', 'spam', 'illegal']
        for word in forbidden_words:
            if word in prompt.lower():
                raise ValueError(f"Prompt contains inappropriate content: {word}")

        return prompt

class SearchResultModel(BaseModel):
    """
    Represents a single search result with structured data
    """
    entity: str = Field(..., description="Original entity/company name")
    extracted_info: str = Field(..., description="Extracted information")
    source_url: Optional[str] = Field(
        default=None,
        description="URL source of the extracted information"
    )
    confidence_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score of the extracted information"
    )
    search_type: SearchType = Field(
        default=SearchType.GENERIC,
        description="Type of search performed"
    )

class BatchSearchResultModel(BaseModel):
    """
    Represents a collection of search results
    """
    results: List[SearchResultModel]
    total_results: int = Field(
        default=0,
        description="Total number of results found"
    )
    processed_entities: List[str] = Field(
        default_factory=list,
        description="List of entities processed"
    )

class ErrorResponseModel(BaseModel):
    """
    Standardized error response model
    """
    error_code: str
    error_message: str
    error_details: Optional[dict] = None

class SearchConfigModel(BaseModel):
    """
    Configuration for search parameters
    """
    use_cache: bool = Field(
        default=True,
        description="Whether to use cached results"
    )
    timeout: int = Field(
        default=30,
        ge=5,
        le=120,
        description="Timeout for search operations in seconds"
    )
    retry_attempts: int = Field(
        default=3,
        ge=0,
        le=5,
        description="Number of retry attempts for failed searches"
    )

# Example usage and validation
def example_validation():
    try:
        # Valid search query
        valid_query = SearchQueryModel(
            column="companies",
            prompt="Find contact email for Google",
            search_type=SearchType.EMAIL,
            limit=5
        )
        print("Valid Query:", valid_query)

        # Invalid query (will raise validation error)
        invalid_query = SearchQueryModel(
            column="",
            prompt="Hack system",
            search_type=SearchType.GENERIC
        )
    except ValueError as e:
        print("Validation Error:", str(e))

if __name__ == "__main__":
    example_validation()
