// src/App.jsx
import React, { useState } from "react";
import { Container, Typography, Alert } from "@mui/material";
import FileUploader from "./components/FileUploader";
import ColumnSelector from "./components/ColumnSelector";
import PromptInput from "./components/PromptInput";
import ResultsTable from "./components/ResultsTable";
import LoadingSpinner from "./components/LoadingSpinner";
import { uploadFile, performSearch } from "./api";

const App = () => {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedColumn, setSelectedColumn] = useState(null);

  const handleFileUpload = async (file) => {
    setLoading(true);
    setError(null);
    try {
      const fileData = await uploadFile(file);
      setUploadedFile(fileData);

      // Automatically select the first column if available
      if (fileData.columns && fileData.columns.length > 0) {
        setSelectedColumn(fileData.columns[0]);
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      setError("Failed to upload file. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleColumnSelect = (column) => {
    setSelectedColumn(column);
  };

  const handlePromptSubmit = async (prompt) => {
    if (!selectedColumn) {
      setError("Please select a column first");
      return;
    }

    setLoading(true);
    setError(null);
    try {
      const searchResults = await performSearch({
        column: selectedColumn,
        prompt: prompt,
        search_type: "generic", // You can modify this based on your needs
        limit: 10,
      });

      setResults(searchResults.results || []);
    } catch (error) {
      console.error("Error performing search:", error);
      setError("Failed to perform search. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" style={{ marginTop: "20px" }}>
      <Typography variant="h4" align="center" gutterBottom>
        AI Data Extractor
      </Typography>

      {error && (
        <Alert
          severity="error"
          onClose={() => setError(null)}
          style={{ marginBottom: "20px" }}
        >
          {error}
        </Alert>
      )}

      <FileUploader onFileUpload={handleFileUpload} />

      {uploadedFile && (
        <>
          <ColumnSelector
            uploadedFile={uploadedFile}
            onColumnSelect={handleColumnSelect}
            selectedColumn={selectedColumn}
          />

          <PromptInput
            onPromptSubmit={handlePromptSubmit}
            disabled={!selectedColumn}
          />

          {loading ? (
            <LoadingSpinner />
          ) : (
            <ResultsTable results={results} columns={uploadedFile.columns} />
          )}
        </>
      )}
    </Container>
  );
};

export default App;
