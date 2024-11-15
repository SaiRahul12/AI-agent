// src/App.js
import React, { useState } from 'react';
import FileUpload from './FileUpload';
import Search from './Search';

const App = () => {
    const [uploadedData, setUploadedData] = useState(null);

    const handleFileUpload = (data) => {
        setUploadedData(data);
    };

    return (
        <div>
            <h1>AI Agent Dashboard</h1>
            <FileUpload onFileUpload={handleFileUpload} />
            {uploadedData && <Search entities={uploadedData.data} />}
        </div>
    );
};

export default App;