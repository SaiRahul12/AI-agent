from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import FileService
from app.services.search_service import SearchService
from app.services.llm_service import LLMService
from app.models.query_models import SearchQueryModel, BatchSearchResultModel, ErrorResponseModel

router = APIRouter()

# Initialize services with your API keys
search_service = SearchService(api_key="2453443b97d6dee7cfe2158f7ab2127eb0a669ca316f7dcee15e187aaccdb789")
llm_service = LLMService(api_key="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")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_data = FileService.read_csv_file(contents)
        return file_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/search", response_model=BatchSearchResultModel, responses={400: {"model": ErrorResponseModel}})
async def perform_search(query: SearchQueryModel):
    try:
        # Perform a web search for the entity
        search_results = await search_service.perform_web_search(query.entity, query.prompt)

        # Extract information using LLM
        extracted_info = await llm_service.extract_information(query.entity, search_results, query.prompt)

        # Return the results
        return BatchSearchResultModel(
            results=search_results,
            extracted_info=extracted_info,
            total_results=len(search_results),
            processed_entities=[result['entity'] for result in search_results]
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseModel(
                error_code="SEARCH_ERROR",
                error_message=str(e)
            )
        )
