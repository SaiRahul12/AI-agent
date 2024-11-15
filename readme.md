AI Agent Backend Project

This project implements a FastAPI backend for an AI agent that processes CSV files, performs web searches, and extracts information using a large language model (LLM).
Project Structure

project_root/

│

├── backend/

│   ├── app/

│   │   ├── __init__.py

│   │   ├── main.py

│   │   ├── routes/

│   │   │   ├── __init__.py

│   │   │   ├── data_routes.py

│   │   ├── services/

│   │   │   ├── __init__.py

│   │   │   ├── file_service.py

│   │   │   ├── search_service.py

│   │   │   ├── llm_service.py

│   │   ├── models/

│   │   │   ├── __init__.py

│   │   │   ├── query_models.py

│   └── requirements.txt

└── frontend/

Installation and Setup
Prerequisites

    Python 3.7 or higher
    pip (Python package installer)
    (Optional) Virtual environment

Step 1: Clone the Repository

Clone the repository to your local machine:

bash

git clone https://github.com/yourusername/ai-agent-backend.git

cd ai-agent-backend/backend

Step 2: Create a Virtual Environment (Optional)

It's recommended to create a virtual environment to manage dependencies.

bash

# Create a virtual environment

python -m venv venv


# Activate the virtual environment

# On Windows

venv\Scripts\activate

# On macOS/Linux

source venv/bin/activate

Step 3: Install Dependencies

Install the required packages using pip:

bash

pip install -r requirements.txt

Step 4: Running the Application

Start the FastAPI application using Uvicorn:

bash

uvicorn app.main:app --reload

The application will be accessible at http://127.0.0.1:8000.
Step 5: Testing the Endpoints

You can test the API endpoints using Postman or cURL.
File Upload Endpoint

To upload a CSV file, use the following cURL command:

bash

curl -X POST "http://127.0.0.1:8000/api/v1/data/upload" \

     -F "file=@/path/to/your/file.csv"

Search Endpoint

To perform a search, use the following cURL command:

bash

curl -X POST "http://127.0.0.1:8000/api/v1/data/search" \

     -H "Content-Type: application/json" \

     -d '{"entity": "Google", "prompt": "Get company email"}'

API Endpoints
1. File Upload Endpoint

    URL: /api/v1/data/upload
    Method: POST
    Description: Uploads a CSV file and returns the columns and data.
    Request Body: Form-data with a file key.
    Response:

    json

{

  "columns": ["column1", "column2"],

  "data": [{"column1": "value1", "column2": "value2"}],

  "row_count": 10

    }

2. Search Endpoint

    URL: /api/v1/data/search
    Method: POST
    Description: Performs a web search and extracts information based on the provided entity and prompt.
    Request Body:

    json

{

  "entity": "Google",

  "prompt": "Get company email"

}

Response:

json

{

  "entity": "Google",

  "search_results": [/* array of search results */],

  "extracted_info": {/* extracted information */}

    }

Project Files Explanation
1. main.py

The entry point of the FastAPI application. It initializes the FastAPI app, sets up CORS, and includes the data routes.
2. data_routes.py

Defines the API endpoints for file upload and search functionality. It uses service classes to handle business logic.
3. file_service.py

Contains logic for processing uploaded files, specifically CSV files.
4. search_service.py

Handles web search functionality, interacting with search APIs.
5. llm_service.py

Contains logic for interacting with the large language model (LLM) API to extract information from search results.
6. query_models.py

Defines data models for request and response schemas, ensuring data validation and serialization.
Environment Variables

For security, sensitive information such as API keys should be stored in environment variables. You can create a .env file in the backend directory and add your keys:

SERPAPI_KEY=your_serpapi_key

OPENAI_KEY=your_openai_key

Make sure to load these variables in your application using a library like python-dotenv.
Additional Features

Feel free to enhance the project by adding features such as:

    Advanced query templates for extracting multiple fields.
    Integration with Google Sheets for output.
    Improved error handling and user notifications.

Troubleshooting

If you encounter issues:

    Ensure all dependencies are installed correctly.
    Check that your API keys are valid and have the necessary permissions.
    Use logging to debug any errors in your service methods.

Conclusion

This guide provides a complete overview of setting up and running the FastAPI backend for the AI agent project. For further assistance, feel free to reach out or consult the FastAPI documentation.