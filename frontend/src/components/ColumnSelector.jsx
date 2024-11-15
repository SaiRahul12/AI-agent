// src/components/ColumnSelector.jsx
import React from "react";
import {
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Paper,
} from "@mui/material";

const ColumnSelector = ({ uploadedFile, onColumnSelect }) => {
  const [selectedColumn, setSelectedColumn] = React.useState("");

  const handleColumnChange = (event) => {
    const column = event.target.value;
    setSelectedColumn(column);
    onColumnSelect(column);
  };

  return (
    <Paper elevation={3} style={{ padding: "20px", marginBottom: "20px" }}>
      <FormControl fullWidth>
        <InputLabel id="column-select-label">Select Column</InputLabel>
        <Select
          labelId="column-select-label"
          value={selectedColumn}
          onChange={handleColumnChange}
        >
          {uploadedFile.columns.map((column) => (
            <MenuItem key={column} value={column}>
              {column}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Paper>
  );
};

export default ColumnSelector;
