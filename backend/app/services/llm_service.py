import openai
from typing import List

class LLMService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def extract_information(self, entity: str, search_results: List[dict], prompt: str) -> str:
        """
        Extract information using OpenAI's API based on search results.

        Args:
            entity (str): The entity for which information is being extracted.
            search_results (List[dict]): List of search results containing snippets.
            prompt (str): The prompt to guide the LLM in extracting information.

        Returns:
            str: The extracted information from the LLM response.
        """
        combined_results = "\n".join([result['snippet'] for result in search_results])

        try:
            response = await openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Extract the information for {entity} from the following results:\n{combined_results}"}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise RuntimeError(f"Failed to extract information: {str(e)}")
