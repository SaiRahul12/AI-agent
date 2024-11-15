import requests
from typing import List, Dict, Any

class SearchService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def perform_web_search(self, entity: str, prompt: str) -> List[Dict[str, Any]]:
        """
        Perform a web search using SerpAPI for the given entity.

        Args:
            entity (str): The entity to search for.
            prompt (str): The search query prompt.

        Returns:
            List[Dict[str, Any]]: A list of search results.
        """
        search_url = f"https://serpapi.com/search.json?q={prompt.format(company=entity)}&api_key={self.api_key}"

        try:
            response = requests.get(search_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('organic_results', [])
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Web search failed: {str(e)}")
