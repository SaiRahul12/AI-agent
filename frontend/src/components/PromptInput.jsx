// src/components/PromptInput.jsx
import React, { useState } from "react";
import { TextField, Paper, Button } from "@mui/material";

const PromptInput = ({ onPromptSubmit }) => {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = () => {
    onPromptSubmit(prompt);
    setPrompt("");
  };

  return (
    <Paper elevation={3} style={{ padding: "20px", marginBottom: "20px" }}>
      <TextField
        label="Enter your search prompt"
        variant="outlined"
        fullWidth
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        style={{ marginBottom: "10px" }}
      />
      <Button variant="contained" onClick={handleSubmit} disabled={!prompt}>
        Submit Prompt
      </Button>
    </Paper>
  );
};

export default PromptInput;
