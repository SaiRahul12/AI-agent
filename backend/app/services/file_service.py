import pandas as pd
from io import BytesIO
from typing import Dict, List, Any

class FileService:
    def read_csv_file(file_contents: bytes) -> Dict[str, Any]:
        """
        Read CSV file contents and return columns and data

        Args:
            file_contents (bytes): Contents of the uploaded file

        Returns:
            Dict containing columns and data
        """
        try:
            df = pd.read_csv(BytesIO(file_contents))
            return {
                "columns": df.columns.tolist(),
                "data": df.to_dict(orient="records")
            }
        except Exception as e:
            raise ValueError(f"Error reading CSV file: {str(e)}")

    @staticmethod
    def validate_file(file_contents: bytes) -> bool:
        """
        Validate the uploaded file

        Args:
            file_contents (bytes): Contents of the uploaded file

        Returns:
            bool: Whether the file is valid
        """
        try:
            df = pd.read_csv(BytesIO(file_contents))
            return len(df) > 0
        except Exception:
            return False

    @staticmethod
    def get_column_names(file_contents: bytes) -> List[str]:
        """
        Get column names from the CSV file

        Args:
            file_contents (bytes): Contents of the uploaded file

        Returns:
            List of column names
        """
        try:
            df = pd.read_csv(BytesIO(file_contents))
            return df.columns.tolist()
        except Exception as e:
            raise ValueError(f"Error extracting column names: {str(e)}")
