// src/components/FileUploader.jsx
import React, { useState } from "react";
import { Button, Typography, Paper } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";

const FileUploader = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (selectedFile) {
      const uploadedData = await uploadFile(selectedFile);
      onFileUpload(uploadedData);
    }
  };

  return (
    <Paper elevation={3} style={{ padding: "20px", marginBottom: "20px" }}>
      <input
        accept=".csv"
        style={{ display: "none" }}
        id="file-upload"
        type="file"
        onChange={handleFileChange}
      />
      <label htmlFor="file-upload">
        <Button
          variant="contained"
          component="span"
          startIcon={<CloudUploadIcon />}
        >
          Upload CSV File
        </Button>
      </label>
      {selectedFile && (
        <Typography variant="body2" style={{ marginTop: "10px" }}>
          Selected: {selectedFile.name}
        </Typography>
      )}
      <Button
        variant="outlined"
        onClick={handleUpload}
        disabled={!selectedFile}
        style={{ marginTop: "10px" }}
      >
        Upload
      </Button>
    </Paper>
  );
};

export default FileUploader;
